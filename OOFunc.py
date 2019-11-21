# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:27:18 2019

@author: Daan
"""
#Functions for Operation Optimization

from os import getcwd,remove

def todo(string):
    return #print(string)

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
            converted+=int(spl[0])*60+int(spl[1])
        elif len(spl) == 1:
            converted+=int(spl[0])*60
        else:
            print('error in timeToMin split')
            return "error in timeToMin split"
    else: 
        return int(numTime)*60
    return converted

def timeTo5Min(Time):
    #Takes input and converts it to slot per 5.
    #Input can be in several formats: hh:mm (5:15), hh (5), hh:mm am/pm (5:15am), hh am/pm
    #spaces do not matter
    converted=timeToMin(Time)
    return int(converted/5)

def generateRunFiles(lpFileName):
    import time 
    #lpFileName is the name of the LP file (without.lp) in the LPFiles directory in the current work directory
    lpFileName=lpFileName.strip(".lp")
    #Get the exact path and name of each file:
    filepath=getcwd()+"\LPFiles"
    CCFPath=filepath+"\\"+lpFileName+"CCF.CCF"
    BatPath=filepath+"\\"+lpFileName+"Run.bat"
    SOLPath=filepath+"\\"+lpFileName+"SOL.SOL"
    LpPath =filepath+"\\"+lpFileName+".lp"
    #Delete sol file before running:
    try:
        remove(SOLPath)
    except:
        removed=1
    #generate CCF:
    f = open(CCFPath,"w+")
    f.write("read "+LpPath+"\n")
    f.write("opt\n")
    f.write("write "+SOLPath+"\n")
    f.write("quit\n")
    f.close() 
    #generate BAT
    f = open(BatPath,"w+")
    f.write('"C:\Program Files\IBM\ILOG\CPLEX_Studio129\cplex\\bin\\x64_win64\cplex.exe" < '+CCFPath)
    f.close()
    
    time.sleep(1)
    
    #run BAT
    from subprocess import Popen
    p = Popen(BatPath)
    p.wait()
    
    time.sleep(1)
    
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
        def __init__(self,terminal,domesticFlight,distanceToTerminal):
            self._registry.append(self) #Add gate to the list of gates
            self.number=len(Gate._registry) #Give terminal a number
            self.terminal = terminal #Link gate to a terminal - Use the terminal Object as input
            self.domesticFlight = domesticFlight #Boolean indicating whether this gate is reserved for domestic flights
            self.distanceToTerminal = distanceToTerminal #distance from gate to Terminal entrance/exit
            self.openEvening = terminal.openEvening #inherit openEvening boolean from Terminal class
            self.distance = distanceToTerminal + terminal.distance #distance from gate to airport entrance/exit
            
class Airline(object):
        _registry = [] #Keep track of all instances
        def __init__(self,name,gatePref):
            self._registry.append(self) #Add terminal to list of terminals
            self.name=name #Give airliner a name A,B,C...
            self.number=len(Airline._registry) #Give terminal a number
            self.gatePref = gatePref #what gate does the airliner prefer
            
class Flight(object):
        _registry = [] #Keep track of all instances
        def __init__(self,identifier,passengers,arrivalTime,departureTime,formFactor,airline):
            self._registry.append(self) #Add this flight to list of flights
            self.number=len(Flight._registry) #Give flight a number
            self.identifier = identifier #Store the flight code of the aircraft
            self.passengers = passengers #Amount of passengers in the aircraft
            self.arrivalTime = arrivalTime #Arrival time of the aircraft
            self.departureTime = departureTime #Departure time of the aircraft
            self.formFactor = formFactor #formFactor of the aircraft (for compliance of aircraft to size constraints)
            self.airline = airline #What airline does the aircraft belong to as an object
            
            #timeSlotsPer5Min
            self.timeSlotBegin = str(timeTo5Min(arrivalTime))
            self.timeSlotEnd = str(timeTo5Min(arrivalTime))
            self.timeSlotBeginBuffer = str(timeTo5Min(arrivalTime)-2)
            self.timeSlotEndBuffer = str(timeTo5Min(arrivalTime)+2)
            
            #Get gatepref
            if airline.gatePref != 0:
                self.gatePref = airline.gatePref.number
            else:
                self.gatePref = 0

def plotTimeTable(data, grid=0, xTickLabels=[],yTicks=True):
    import matplotlib.pyplot as plt
    import numpy as np
    #Plot the input data [an array with rows being the time gates and the cols
    #being the timeslot] in a timetable-like way.
    #
    #grid is a boolean deciing whether or not grid lines are shown
    #
    #xTickLabels is a list of labels to be distributed equally over the Xaxis
    #according to their ratio and modulus.
    #e.g. a dataset with 7 columns and timesteps of 15 minutes starting at 12pm
    #would end at 1:45pm, giving xTickLabels=["12pm","1am"] as input would give
    #the proper result. 
    #So if the first label is the time at which your dataset starts and you simply
    #include all following labels that are still within your data set the program
    #will take care of the rest :)
    #
    #yTicks adds ticks with Gate 1, 2 etc. to the side, requires Grid=1
    #======================================================
    
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
    
    if yTicks==True:
        yTicksList=[]
        for i in range(height):
            yTicksList.append("Gate "+str(i+1))
        ax.axes.yaxis.set_ticklabels(yTicksList)
        
    #Process xTickLabels list into properly distributed list
    xTickLabelsProcessed=[] #List for the actual to be used labels
    if len(xTickLabels)!=0: #If lists is not equal to zero it needs to be processed.
        labels=len(xTickLabels) #Amount of labels to assign
        reqLabels=width+1 #Amount of tick labels needed
        mod=reqLabels%labels #Amount of spots after the last label
        r=labels/(reqLabels-mod) #Ratio between labels and required labels, used to find the amount of empty labels
        for i in range(labels): #For each input label:
            xTickLabelsProcessed.append(xTickLabels[i]) #Append the label
            for j in range(int(1/r)-1): #Append the required empty labels
                xTickLabelsProcessed.append('')
        for i in range(int(mod)):
            xTickLabelsProcessed.append('') #Apply the final empty values.
    ax.axes.xaxis.set_ticklabels(xTickLabelsProcessed) #assign the found list 

    #Set up colors for y axis (Gates)
    #Colors are spaced over a rainbow color map, as far apart as possible for
    #the sake of clarity
    colors=[]
    cm = plt.get_cmap('gist_rainbow')
    for i in range(height):
        colors.append(cm(1.*i/height))    
    
    #Finally make the actual plot
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            #Get coordinators of corners for the square
            x1 = [x, x+1]
            y1 = np.array([y, y])
            y2 = y1+1
            #If the list item is NOT zero, assign it.
            if col != 0: 
                plt.fill_between(x1, y1, y2=y2, color=colors[y]) #Make colored square
                plt.text((x1[0]+x1[1])/2, (y1[0]+y2[0])/2, #Place text, in center of square
                         str(col),
                         horizontalalignment='center',
                         verticalalignment='center')
    plt.show() #Victory
    
#data = [["a", 0 ,"d","d","f","f", 0 ],
#        [ 0 ,"b","b", 0 ,"e", 0 ,"g"],
#        [ 0 , 0 ,"c","c","c","h", 0 ],
#        [ 0 , 0 ,"i","i", 0 ,"j","k"]]
#
#plotTimeTable(data,1,["12pm","1pm"])