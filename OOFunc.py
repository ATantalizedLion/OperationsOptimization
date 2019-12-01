# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:27:18 2019

@author: Daan
"""
#Functions for Operation Optimization

from os import getcwd,remove
import numpy as np
import random

def todo(string):
    return print(string)

def timeToMin(Time):
    #Takes input and converts it to minutes.
    #Input can be in several formats: hh:mm (5:15), hh (5), hh:mm am/pm (5:15am), hh am/pm
    #spaces do not matter
    converted=0
    if Time.find('pm')!=-1:
        #add 12 hours to time if pm
        converted+=12*60
        #Get rid of am and pm since they have been used
    numTime=Time.strip('am')
    numTime=numTime.strip('pm')
    numTime=numTime.strip(' ')
    if Time.find(':')!=-1:
        # ':' is found.
        # split time in hh:mm format into seperate items
        spl=numTime.split(':')
        if len(spl) == 2:
            if spl[0] == 12:
                converted+=int(spl[1])
            else:
                converted+=int(spl[0])*60+int(spl[1])
        elif len(spl) == 1:
            if int(spl) == 12:
                converted += 0
            else:
                converted+=int(spl[0])*60
        else:
            print('error in timeToMin split')
            return "error in timeToMin split"
    else: 
        if int(numTime)==12:
            converted += 0
        else:
            converted+=int(numTime)*60
    return converted

def timeTo5Min(Time):
    #Takes input and converts it to slot per 5.
    #Input can be in several formats: hh:mm (5:15), hh (5), hh:mm am/pm (5:15am), hh am/pm
    #spaces do not matter
    converted=timeToMin(Time)
    return int(converted/5)

def minToTime(minutes):
    h = int(minutes/60)
    m = minutes - h*60
    if len(str(m)) == 1:
        mm = '0'+str(m)
    else:
        mm = m
    converted = str(h)+":"+str(mm)
    return converted

def fiveMinToTime(fiveMin):
    return minToTime(fiveMin*5)

def generateRunFiles(lpFileName):
    
    #lpFileName is the name of the LP file (without.lp) in the LPFiles directory in the current work directory
    lpFileName=lpFileName.strip(".lp")
    #Get the exact path and name of each file:
    filepath=getcwd()+"\LPFiles"
    CCFPath=filepath+"\\"+lpFileName+"CCF.CCF"
    BatPath=filepath+"\\"+lpFileName+"Run.bat"
    SOLPath=filepath+"\\"+lpFileName+"SOL.SOL"
    LpPath =filepath+"\\"+lpFileName+".lp"
    logPath=getcwd()+"\cplex.log"
    #Delete sol file before running:
    try:
        remove(SOLPath)
    except:
        removed=1
    #Delete log file before running:
    try:
        remove(logPath)
    except:
        removed=1
    #generate CCF:
    f = open(CCFPath,"w+")
    f.write('read "'+LpPath+'"\n')
    f.write("opt\n")
    f.write('write "'+SOLPath+'"\n')
    f.write("quit\n")
    f.close() 
    #generate BAT
    f = open(BatPath,"w+")
    f.write('"C:\Program Files\IBM\ILOG\CPLEX_Studio129\cplex\\bin\\x64_win64\cplex.exe" < '+ '"'+CCFPath+'"')
    f.close()
    #run BAT
    from subprocess import Popen
    p = Popen(BatPath)
    p.wait()
    
    #cleanUpCCFandBAT:
    remove(BatPath)
    remove(CCFPath)
    return SOLPath

class Terminal(object):
        _registry = [] #Keep track of all instances
        def __init__(self,name,openEvening,distance):
            self._registry.append(self) #Add terminal to list of terminals
            self.name=name #Give terminal a name A,B,C...
            self.number=len(Terminal._registry) #Give terminal a number
            self.openEvening = openEvening #Is the gate open past 6 pm
            self.distance = distance#Distance from terminal to exit of airport
            
class Gate(object):
        _registry = [] #Keep track of all instances
        finalEveningClosedNumber = 0 #highest number of gates closed in the evening
        finalDomesticNumber = 0
        def __init__(self,terminal,domesticGate,distanceToTerminal):
            self._registry.append(self) #Add gate to the list of gates
            self.number = len(Gate._registry) #Give gate a number
            self.terminal = terminal #Link gate to a terminal - Use the terminal Object as input
            if terminal.openEvening == False:
                Gate.finalEveningClosedNumber = self.number
                
            self.domesticGate = domesticGate #Boolean indicating whether this gate is reserved for domestic flights
            if self.domesticGate == 1:
                Gate.finalDomesticNumber = self.number
                
            self.distanceToTerminal = distanceToTerminal #distance from gate to Terminal entrance/exit
            self.openEvening = terminal.openEvening #inherit openEvening boolean from Terminal class
            self.distance = distanceToTerminal + terminal.distance #distance from gate to airport entrance/exit

class Bay(object):
        _registry = [] #Keep track of all instances
        def __init__(self,linkedGates,linkedGatesDistances,formFactor,refuelBay=True,serviceBay=False,remoteBay=False):
            self._registry.append(self) #Add gate to the list of gates
            self.number = len(Bay._registry) #Give Bay a number
            self.linkedGates = linkedGates #All gates linked to this one.
            self.linkedGatesDistances = linkedGatesDistances
            self.formFactor = formFactor
            self.serviceBay = serviceBay #Whether or not bay can perform any servicing
            self.remoteBay = remoteBay #requires busses and other resources
            self.refuelBay = refuelBay #wheteher or not the gate can refuel aircraft
            
class Airline(object):
        _registry = [] #Keep track of all instances
        def __init__(self,name,gatePref=0):
            self._registry.append(self) #Add terminal to list of terminals
            self.name=name #Give airline a name A,B,C...
            self.number=len(Airline._registry) #Give airline a number
            self.gatePref = gatePref #what gate does the airline prefer (default none)
            
class Flight(object):
        _registry = [] #Keep track of all instances
        domFlights = 0 #amount of domestic flights
        finalDomFlight = 0 #Number of the last domestic flight

        def __init__(self,identifier,passengers,arrivalTime,departureTime,formFactor,airline,assignedGate=0,domestic=0):
            self._registry.append(self) #Add this flight to list of flights
            self.number=len(Flight._registry) #Give flight a number
            self.identifier = identifier #Store the flight code of the aircraft
            self.passengers = passengers #Amount of passengers in the aircraft
            self.arrivalTime = arrivalTime #Arrival time of the aircraft
            self.departureTime = departureTime #Departure time of the aircraft
            self.formFactor = formFactor #formFactor of the aircraft (for compliance of aircraft to size constraints)
            self.airline = airline #What airline does the aircraft belong to as an object
            self.domestic = domestic #Domestic or international
            if domestic == 1:
                Flight.domFlights += 1
                Flight.finalDomFlight = self.number
            #timeSlotsPer5Min
            self.timeSlotBegin = timeTo5Min(arrivalTime)
            self.timeSlotEnd = timeTo5Min(departureTime)
            self.timeSlotBeginBuffer = timeTo5Min(arrivalTime)-2
            self.timeSlotEndBuffer = timeTo5Min(departureTime)+2
            
            #for arrival emptying the aircraft is taken to take 15 minutes
            self.timeSlotBeginEmpty = self.timeSlotBegin + 0 #End of arrival/end of boarding time slot
            self.timeSlotEndEmpty = self.timeSlotBegin + 3 #End of arrival/end of boarding time slot
            #boarding is taken to take 30 minutes
            self.timeSlotBeginBoard = self.timeSlotEnd - 3 #Start of boarding
            self.timeSlotEndBoard = self.timeSlotEnd #Start of boarding
            
            #Get gatepref of related airline
            if airline.gatePref != 0:
                self.gatePref = airline.gatePref.number
            else:
                self.gatePref = 0
                
        #Assign a gate:
        def assignGate(self,gate):
            self.assignedGate=gate 
        #Assign a Bay
        def assignBay(self,bay):
            self.assignedBay=bay 

def plotTimetable(data, grid=0, xTickLabels=[], xTickSpacing=0, yTickLabels=True, bays=0):
    import matplotlib.pyplot as plt
    import numpy as np
    #Plot the input data [an array with rows being the time gates and the cols
    #being the timeslot] in a timetable-like way.
    #
    #grid is a boolean deciing whether or not grid lines are shown
    #
    #xTickLabels is a list of labels to be distributed equally over the Xaxis
    #according to xTickSpacing.
    #e.g. a dataset with 7 columns and timesteps of 15 minutes starting at 12pm
    #would end at 1:45pm, giving xTickLabels=["12pm","1pm"] as input with a
    #tickspacing of 3 would give the proper result.
    #
    #yTicks adds ticks with Gate 1, 2 etc. to the side, requires Grid=1
    #======================================================
    flList = []
    flPlottedList = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i,j] != 0:    
                #Try if flight is there:
                try:
                    ind = flList.index(data[i,j].split(' - ')[0])
                except: 
                    flList.append(data[i,j].split(' - ')[0])

    flCountArrList = [0]*len(flList)
    flCountDepList = [0]*len(flList)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i,j] != 0:
                ind = flList.index(data[i,j].split(' - ')[0])
                if data[i,j].split(' - ')[1] == 'Dep':
                    flCountDepList[ind]+=1
                elif data[i,j].split(' - ')[1] == 'Arr':
                    flCountArrList[ind]+=1
                
    #Set up figure
    width=len(data[0])
    height=len(data)
    fig = plt.figure() 
    ax = fig.add_subplot(111)
    plt.ylim(height,0) #Fit to Y, put gate 1 at the top
    plt.xlim(0,width) #Fit to X
    ax.set_aspect(1) #Make square

    #Process grid input/output
    if grid==0:
        ax.axes.get_yaxis().set_visible(False) #Hide all Y axis things (grid, labels)
    else:
        ax.axes.yaxis.set_ticklabels([]) #Hide labels
        ax.set_xticks(np.arange(0,width+1, 1)) #Set X tick spacing
        ax.set_yticks(np.arange(0,height+1, 1)) #Set Y tick spacing
        plt.grid(color='black') #Make lines less ugly
        ax.set_axisbelow(True) #Grid UNDER other stuff
    
    if yTickLabels==True:
        yTicksList=[]
        for i in range(height):
            if bays == 1:    
                yTicksList.append("Bay "+str(i+1))
            else:
                yTicksList.append("Gate "+str(i+1))
            ax.axes.yaxis.set_ticklabels(yTicksList, fontsize = 14, va='top')
        
    #Process xTickLabels list into properly distributed list
    xTickLabelsProcessed=[] #List for the actual to be used labels
    if len(xTickLabels)!=0: #If lists is not equal to zero it needs to be processed.
        if xTickSpacing!=0:
            for label in xTickLabels:
                xTickLabelsProcessed.append(label)
                for i in range(xTickSpacing):
                    xTickLabelsProcessed.append('')
                ax.axes.xaxis.set_ticklabels(xTickLabelsProcessed, fontsize = 14)
        else:
            ax.axes.xaxis.set_ticklabels(xTickLabels)

    ax.axes.xaxis.set_ticklabels(xTickLabelsProcessed) #assign the found list 
    
    #Set up colors for Flights
    #Colors are spaced over a rainbow color map, as far apart as possible for
    #the sake of clarity
    colors=[]
    cm = plt.get_cmap('gist_rainbow')
    for i in range(len(flList)):
        colors.append(cm(1.*i/len(flList)))    
    
    #Finally make the actual plot
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            #Get coordinators of corners for the square
            y1 = np.array([y, y])
            y2 = y1+1
            #If the list item is NOT zero, assign it.
            if col != 0: 
                try:
                    flPlottedList.index(col)
                except:
                    ind = flList.index(col.split(' - ')[0])
                    if col.split(' - ')[1] == 'Dep':
                        count = flCountDepList[ind]
                    elif col.split(' - ')[1] == 'Arr':
                        count = flCountArrList[ind]
                    x1 = [x, x+count]    
                    block = plt.fill_between(x1, y1, y2=y2, color=colors[ind]) #Make colored square
                    block.set_ec('black')
                    plt.text((x1[0]+x1[1])/2, (y1[0]+y2[0])/2, #Place text, in center of square
                             str(col),
                             horizontalalignment='center',
                             verticalalignment='center')
                    flPlottedList.append(col)
    plt.show() #Victory
    

def getTimetableMatrixGates(timeStart,timeEnd,amountGates):
    tStart=timeTo5Min(timeStart)
    tEnd=timeTo5Min(timeEnd)
    dTime=tEnd-tStart
    timeTableMatrix=np.zeros((amountGates,dTime),dtype=object)
    for fl in Flight._registry:
        #Departure procedures
        t1=fl.timeSlotBeginBoard-tStart
        t2=fl.timeSlotEndBoard-tStart
        #Arrival procedures
        ga=fl.assignedGate
        gaNum=ga.number
        gaInd=gaNum-1
        #Arrival
        savedText = str(fl.identifier) + " - Arr"
        if t2 > dTime:
            t2=dTime  #end plotting at end of line
        if t1 <= 0 and t2 <= 0:
            do="nothing" #Ends before plotting no need to do anything
        elif t1 < 0 and t2 >= 0: 
            #for assigned gate, assign flight identifier to gate
            #from slot 0 to slot t2
            for i in range(t2):
                timeTableMatrix[gaInd,i]=savedText # 
        else: #if t1 >0, t2>0 -> plot
            #for assigned gate, assign flight identifier to gate
            #from slot 1 to slot t2
            for i in range(t1,t2):
                timeTableMatrix[gaInd,i]=savedText
        #Departure
        t1=fl.timeSlotBeginEmpty-tStart
        t2=fl.timeSlotEndEmpty-tStart
        savedText = str(fl.identifier) + " - Dep"
        if t2 > dTime:
            t2=dTime  #end plotting at end of line
        if t1 <= 0 and t2 <= 0:
            do="nothing" #Ends before plotting no need to do anything
        elif t1 < 0 and t2 >= 0: 
            #for assigned gate, assign flight identifier to gate
            #from slot 0 to slot t2
            for i in range(t2):
                timeTableMatrix[gaInd,i]=savedText # 
        else: #if t1 >0, t2>0 -> plot
            #for assigned gate, assign flight identifier to gate
            #from slot 1 to slot t2
            for i in range(t1,t2):
                timeTableMatrix[gaInd,i]=savedText
    return timeTableMatrix

def getTimetableMatrixBays(timeStart,timeEnd,amountBays,showGate=0):
    tStart=timeTo5Min(timeStart)
    tEnd=timeTo5Min(timeEnd)
    dTime=tEnd-tStart
    timeTableMatrix=np.zeros((amountBays,dTime),dtype=object)
    for fl in Flight._registry:
        t1=fl.timeSlotBegin-tStart
        t2=fl.timeSlotEnd-tStart
        bay=fl.assignedBay
        bayNum=bay.number
        bayInd=bayNum-1
        savedText = str(fl.identifier) 
        if showGate == 1:
            savedText +=' - Gate' + str(fl.assignedGate.number) 
        if t2 > dTime:
            t2=dTime
        if t1 <= 0 and t2 <= 0:
            do="nothing"
        elif t1 < 0 and t2 >= 0: 
            #for assigned gate, assign flight identifier to gate
            #from slot 0 to slot t2
            for i in range(t2):
                timeTableMatrix[bayInd,i]=savedText
        else: #if t1 >0, t2>0
            #for assigned gate, assign flight identifier to gate
            #from slot 1 to slot t2
            for i in range(t1,t2):
                timeTableMatrix[bayInd,i]=savedText
    return timeTableMatrix

class Airport(object): #for randomizer
        _registry = [] #Keep track of all instances
        def __init__(self,name,shortName,distanceCategory=3):
            self._registry.append(self) #Add gate to the list of gates
            self.number = len(Airport._registry) #Give City a number
            self.name   = name 
            self.shortName = shortName
            self.distanceCategory = distanceCategory
                #0 = Domestic (size C (small)) 
                #1 = Domestic (size B (medium))
                #2 = International nearby (B-C)
                #3 = International med dist (A-B-C)
                #4 = International far (A-B)
                #5 = Intercontinental, A only (large)
            if distanceCategory <= 1:
                self.domestic = True
            else:
                self.domestic = False

def getFlights(flightsWanted,timeStart,timeEnd):
    #generates X amounts of flights from all loaded airports to the destination airport. 
    #Does so with arrival time between timeStart and timeEnd
    timeStart = timeTo5Min(timeStart)
    timeEnd = timeTo5Min(timeEnd)
    for i in range(flightsWanted):
    #    random.seed('givemeflights')
        air = Airport._registry[random.randint(0,len(Airport._registry)-1)]
        flName=str(air.shortName+str(i+1)) #retrieve name from airport object:
        flAirline=  Airline._registry[random.randint(0,len(Airline._registry)-1)]
        #Size categories defined in airport class above
        if air.distanceCategory==0:
            flFF = "C"
            flDomestic=True
        if air.distanceCategory==1:
            flFF = "B"
            flDomestic=True
        if air.distanceCategory==2:
            r = random.randint(0,1)
            if r == 0:
                flFF = "B"
            else: 
                flFF = "C"
            flDomestic=False
        if air.distanceCategory==3:
            r = random.randint(0,2)
            if r == 0:
                flFF = "A"
            elif r ==1: 
                flFF = "B"
            else: 
                flFF = "C"
            flDomestic=False
        if air.distanceCategory==4:
            r = random.randint(0,1)
            if r == 0:
                flFF = "A"
            else: 
                flFF = "B" 
            flDomestic=False
        if air.distanceCategory==5:
            flFF = "A"
            flDomestic=False
            
    #    get amount of passengers 
        if flFF == "A": #300-450
            flPass = random.randrange(300,450)
        if flFF == "B": #150-300
            flPass = random.randrange(150,300)
        if flFF == "C": #50-150
            flPass = random.randrange(50,150)
        
        #work in 5 min slots
    
        flArr = random.randrange(timeStart,timeEnd)
        flDep = flArr + random.randint(5,24) # stays 20 to 120 minutes
    
        Flight(flName, flPass, fiveMinToTime(flArr), fiveMinToTime(flDep), flFF, flAirline,domestic=flDomestic)
    return



def plotTimetable2(data, grid=0, xTickLabels=[], xTickSpacing=0,yTickLabels=True,bays=0):
    import matplotlib.pyplot as plt
    import numpy as np
    #Plot the input data [an array with rows being the time gates and the cols
    #being the timeslot] in a timetable-like way.
    #
    #grid is a boolean deciing whether or not grid lines are shown
    #
    #xTickLabels is a list of labels to be distributed equally over the Xaxis
    #according to xTickSpacing.
    #e.g. a dataset with 7 columns and timesteps of 15 minutes starting at 12pm
    #would end at 1:45pm, giving xTickLabels=["12pm","1pm"] as input with a
    #tickspacing of 3 would give the proper result.
    #
    #yTicks adds ticks with Gate 1, 2 etc. to the side, requires Grid=1
    #======================================================
    flList = []
    flCountList = []
    flPlottedList = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            try:
                ind = flList.index(data[i,j])
                flCountList[ind]+=1
            except: 
                flList.append(data[i,j])
                flCountList.append(1)
                
    #Set up figure
    width=len(data[0])
    height=len(data)
    fig = plt.figure() 
    ax = fig.add_subplot(111)
    plt.ylim(height,0) #Fit to Y, put gate 1 at the top
    plt.xlim(0,width) #Fit to X
    ax.set_aspect(1) #Make square

    #Process grid input/output
    if grid==0:
        ax.axes.get_yaxis().set_visible(False) #Hide all Y axis things (grid, labels)
    else:
        ax.axes.yaxis.set_ticklabels([]) #Hide labels
        ax.set_xticks(np.arange(0,width+1, 1)) #Set X tick spacing
        ax.set_yticks(np.arange(0,height+1, 1)) #Set Y tick spacing
        plt.grid(color='black') #Make lines less ugly
        ax.set_axisbelow(True) #Grid UNDER other stuff
    
    if yTickLabels==True:
        yTicksList=[]
        for i in range(height):
            if bays == 1:    
                yTicksList.append("Bay "+str(i+1))
            else:
                yTicksList.append("Gate "+str(i+1))
            ax.axes.yaxis.set_ticklabels(yTicksList, fontsize = 14, va='top')
        
    #Process xTickLabels list into properly distributed list
    xTickLabelsProcessed=[] #List for the actual to be used labels
    if len(xTickLabels)!=0: #If lists is not equal to zero it needs to be processed.
        if xTickSpacing!=0:
            for label in xTickLabels:
                xTickLabelsProcessed.append(label)
                for i in range(xTickSpacing):
                    xTickLabelsProcessed.append('')
                ax.axes.xaxis.set_ticklabels(xTickLabelsProcessed, fontsize = 14)
        else:
            ax.axes.xaxis.set_ticklabels(xTickLabels)

    ax.axes.xaxis.set_ticklabels(xTickLabelsProcessed) #assign the found list 
    
    #Set up colors for Flights
    #Colors are spaced over a rainbow color map, as far apart as possible for
    #the sake of clarity
    colors=[]
    cm = plt.get_cmap('gist_rainbow')
    for i in range(len(flList)):
        colors.append(cm(1.*i/len(flList)))    
    
    #Finally make the actual plot
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            #Get coordinators of corners for the square
            y1 = np.array([y, y])
            y2 = y1+1
            #If the list item is NOT zero, assign it.
            if col != 0: 
                try:
                    flPlottedList.index(col)
                except:
                    ind = flList.index(col)
                    x1 = [x, x+flCountList[ind]]    
                    ind = flList.index(col)
                    block = plt.fill_between(x1, y1, y2=y2, color=colors[ind]) #Make colored square
                    block.set_ec('black')
                    plt.text((x1[0]+x1[1])/2, (y1[0]+y2[0])/2, #Place text, in center of square
                             str(col),
                             horizontalalignment='center',
                             verticalalignment='center')
                    flPlottedList.append(col)
    plt.show() #Victory

