# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:21:08 2019

@author: Daan
"""

#import matplotlib.pyplot as plt
import numpy as np
from OOFunc import generateRunFiles, timeTo5Min, fiveMinToTime, getTimetableMatrixGates, plotTimetableBays, plotTimetableGates, getTimetableMatrixBays, Flight, Airline, Airport, Gate, Terminal, Bay, todo, getFlights
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

plt.close("all")

#Use the old nonrandomized data (0/1)

#0 - Dynamic data set
#1 - Static data set 
#2 - last generated data set again
#3 - simplified dataset 
staticDataSet = 1


#If 0, generate random dataset with following properties:
timeStart = "2pm"
timeEnd = "6pm"
flightsWanted= 20

#plot results?
plotResults = 0

plotTimeStart = "3pm" #in full hours #5pm for static
plotTimeEnd = "11pm" #in full hours #11pm for static

if staticDataSet == 0 or staticDataSet == 1 or staticDataSet == 2:
    #Terminal(name,openEvening,distance)
    t1 = Terminal("A",True,250)
    t2 = Terminal("B",True,610)
    t3 = Terminal("C",True,460)
    t4 = Terminal("D",False,100)
    
    #Gate(terminal,domesticGate,distanceToTerminal)
    g1 = Gate(t1,True,100)
    g2 = Gate(t1,False,300)
    g3 = Gate(t1,True,100)
    g4 = Gate(t1,False,300)
    
    g5 = Gate(t2,False,100)
    g6 = Gate(t2,False,400)
    g7 = Gate(t2,False,700)
    
    g8 = Gate(t3,False,100)
    g9 = Gate(t3,False,400)
    g10 = Gate(t3,False,700)
    
    g11 = Gate(t4,False,380)
    g12 = Gate(t4,False,80)
    
    #Bay(linkedGates,distLinkedGates,formFactor)
    b1 = Bay([g1,g3],[100,150],"B")
    b2 = Bay([g1,g3],[150,100],"B")
    b3 = Bay([g2,g4],[100,150],"B")
    b4 = Bay([g2,g4],[150,100],"B")
    
    b5 = Bay([g5,g6],[100,150],"A")
    b6 = Bay([g5,g6],[150,100],"A")
    b7 = Bay([g6,g7],[100,150],"A")
    b8 = Bay([g6,g7],[150,100],"A")
    
    b9  = Bay([g8,g9],[150,100],"A")
    b10 = Bay([g8,g9],[100,150],"A")
    b11 = Bay([g9,g10],[150,100],"A")
    b12 = Bay([g9,g10],[100,150],"A")
    
    b13 = Bay([g11],[100],"B")
    b14 = Bay([g11,g12],[100,100],"B")
    b15 = Bay([g11,g12],[100,100],"B")
    b16 = Bay([g12],[100],"B")
    
    #remote bays 
    b17 = Bay([g1,g3,g5,g6,g7],[600,600,600,600,600],"A")
    b18 = Bay([g1,g3,g5,g6,g7],[600,600,600,600,600],"B")
    b19 = Bay([g1,g3,g5,g6,g7],[600,600,600,600,600],"C")
    
    #Airliner(name,gatePref)
    AirFrance   = Airline("AirFrance",g5)
    KLM = Airline("KLM",g8)
    Delta = Airline("Delta",g11)
    BritishAirways=Airline("British Airways")
    Transavia=Airline("Transavia")
    EasyJet = Airline("EasyJet")

elif staticDataSet == 3: 
    t1 = Terminal("A",True,250)
    
    g1 = Gate(t1,True,100)
    g2 = Gate(t1,False,300)
    g3 = Gate(t1,True,100)
    g4 = Gate(t1,False,300)
    
    b1 = Bay([g1,g3],[100,150],"B")
    b2 = Bay([g1,g3],[150,100],"B")
    b3 = Bay([g2,g4],[100,150],"B")
    b4 = Bay([g2,g4],[150,100],"C")
    #Airliner(name,gatePref)
    KLM = Airline("KLM")
    Transavia=Airline("Transavia")
    


#init airports for flight schedule randomizer:
#distances as if a second large airport in the Netherlands would exist
#Airport(name,shortname,distanceCategory)
Airport("Amsterdam Schiphol Airport","AMS",1)
Airport("Lelystad Airport","LEY",0)
Airport("Berlin Regional Airport","BML",2)
Airport("Brussels Airport (Zaventem Airport)", "BRU", 2)
Airport("Barcelona - EL Prat Airport", "BLN", 3)
Airport("Collective of NY airports","NYC",5)
Airport("Collective of London airports", "LON", 3)
Airport("Collective of Paris airports", "PAR", 2)
Airport("Collective of Rome airports", "ROM", 4)
Airport("Sydney Airport (Kingsford Smith Airport)", "SYD",5)

if staticDataSet == 1:
    #Flight(identifier,passengers,arrivalTime,departureTime,formFactor,airliner)
    fl1 = Flight("JFK24", 200, "5:25pm","6:35pm","B",EasyJet)
    fl2 = Flight("JFK26", 100, "5:55pm", "7:05pm","C",Delta,needToRefuel=True)
    fl3 = Flight("JFK27", 100, "6:05pm", "7:10pm","C",BritishAirways)
    fl4 = Flight("JFK28", 300, "6pm", "6:30pm","C",Transavia)
    fl5 = Flight("JFK29", 100, "6:25pm", "7:20pm","C",Transavia)
    fl6 = Flight("JFK31", 300, "6:35pm", "7:45pm","A",Transavia)
    fl7 = Flight("JFK35", 100, "7:15pm", "8:55pm","C",KLM)
    fl8 = Flight("JFK36", 300, "7:30pm", "9:05pm","A",Transavia)
    fl9 = Flight("DOM37", 100, "7:45pm", "9:20pm","C",BritishAirways, domestic=1)
    fl10 = Flight("DOM38", 200, "8:15pm", "10:05pm","B",EasyJet,domestic = 1)
    fl11 = Flight("JFK32", 200, "5:10pm", "5:55pm","B",KLM)
    fl12 = Flight("JFK33", 100, "5:30pm", "5:05pm","C",KLM)
    fl13 = Flight("JFK34", 200, "8:05pm", "8:50pm","B",KLM)
    fl14 = Flight("JFK30", 100, "6:30pm", "7:30pm","C",AirFrance)
    fl15 = Flight("DOM23", 300, "5:15pm","6pm","A",KLM,domestic=1)
elif staticDataSet == 2:
    import lastGeneratedDataset
elif staticDataSet == 0:
    getFlights(flightsWanted,timeStart,timeEnd)
elif staticDataSet == 3:
    fl1 = Flight("DOM01", 200, "3:00pm", "4:00pm","B",KLM, domestic=1)
    fl2 = Flight("DOM02", 100, "3:00pm", "4:00pm","B",KLM, domestic=1)
    fl8 = Flight("JFK01", 200, "3:00pm", "4:00pm","B",Transavia)
    fl8 = Flight("JFK02", 100, "3:00pm", "4:00pm","C",Transavia)
    
    
timemat = np.zeros((len(Flight._registry),len(Flight._registry))) #Generating time overlap matrix for full stay of aircraft
i = 0
for fl in Flight._registry:
    j = 0
    for fl2 in Flight._registry:
        overlap = int(fl.timeSlotEndBuffer) - int(fl2.timeSlotBeginBuffer)
        if overlap >= 0 and int(fl2.timeSlotEndBuffer) > int(fl.timeSlotBeginBuffer):
            timemat[i][j] = 1
        j += 1
    i += 1
    
timematArr = np.zeros((len(Flight._registry),len(Flight._registry))) #Generating time overlap matrix for full stay of aircraft
i = 0
for fl in Flight._registry:
    j = 0
    for fl2 in Flight._registry:
        overlap = int(fl.timeSlotEndEmpty) - int(fl2.timeSlotBeginBoard)
        if overlap >= 0 and int(fl2.timeSlotEndBoardBuffer) > int(fl.timeSlotBeginEmptyBuffer):
            timematArr[i][j] = 1
        overlap2 = int(fl.timeSlotEndEmpty) - int(fl2.timeSlotBeginEmptyBuffer)
        if overlap2 >= 0 and int(fl2.timeSlotEndEmpty) > int(fl.timeSlotBeginEmptyBuffer):
            timematArr[i][j] = 1
        j += 1
    i += 1
    
timematDep = np.zeros((len(Flight._registry),len(Flight._registry))) #Generating time overlap matrix for full stay of aircraft
i = 0
for fl in Flight._registry:
    j = 0
    for fl2 in Flight._registry:
        overlap = int(fl.timeSlotEndBoardBuffer) - int(fl2.timeSlotBeginBoard)
        if overlap >= 0 and int(fl2.timeSlotEndBoardBuffer) > int(fl.timeSlotBeginBoard):
            timematDep[i][j] = 1
        overlap2 = int(fl.timeSlotEndBoardBuffer) - int(fl2.timeSlotBeginEmptyBuffer)
        if overlap2 >= 0 and int(fl2.timeSlotEndEmpty) > int(fl.timeSlotBeginBoard):
            timematDep[i][j] = 1
        j += 1
    i += 1

#intialize useful Variables
amountFlights=len(Flight._registry)
amountGates=len(Gate._registry)
amountBays=len(Bay._registry)
    
#list for binary generation
binlist=[]
for fl in Flight._registry:
    for bay in Bay._registry:
        curXIK=str("X_I"+str(fl.number)+"_K"+str(bay.number))
        binlist.append(curXIK)
    for ga in Gate._registry:
        curXIL=str("X_I"+str(fl.number)+"_L"+str(ga.number))
        binlist.append(curXIL)
    for bay in Bay._registry:
        for ga in bay.linkedGates:
            curXIKL=str("X_I"+str(fl.number)+"_K"+str(bay.number)+"_L"+str(ga.number))
            binlist.append(curXIKL)
            
#I=flights
#K=bays
#L=gates

#RUN CPlex
    #Take input flights and generate LP file
    
todo("Implement objective function weights and priorities (currently they are pretty random)") 

with open("LPFiles\SecondIteration.lp","w+") as f:

    #generate Objective
    f.write("Minimize multi-objectives\n") #Z1 = sum_i sum_k Pi*Xi,k*Dterm_k
    f.write("OBJ1: Priority=1 Weight=1.0 Abstol=0.0 Reltol=0.0\n\n") #Choose gate closest to terminal exit, weighed by passengers in flight
    for fl in Flight._registry:
        for ga in Gate._registry:
           f.write(str(fl.passengers*ga.distanceToTerminal)) 
           f.write(" X_I"+str(fl.number)+"_L"+str(ga.number))
           if int(fl.number)!=int(amountFlights) or int(ga.number)!=int(amountGates):
              f.write(" + ") 
           else:
              f.write("")

    f.write("\n")
    f.write("\n")
    f.write("OBJ2: Priority=2 Weight=1.0 Abstol=0.0 Reltol=0.0\n\n") #Maximize gate preference
    for fl in Flight._registry: #Z2 = sum_i sum_k Xi,k * Dterm_k
        for ga in Gate._registry:
           if int(fl.gatePref)==ga.number:
               f.write("-")#+str(1))
               f.write(" X_I"+str(fl.number)+"_L"+str(ga.number)+" ")

    f.write("\n")
    f.write("\n")    
    f.write("OBJ3: Priority=1 Weight=2.0 Abstol=0.0 Reltol=0.0\n\n") #Minimize gate - bay distance , weighed by passengers in flight
    for fl in Flight._registry:
        for bay in Bay._registry:
           for i in range(len(bay.linkedGates)):
               ga=bay.linkedGates[i]
               gaDist=bay.linkedGatesDistances[i] 
               f.write(str(fl.passengers*gaDist))
               f.write(" X_I"+str(fl.number)+"_K"+str(bay.number)+"_L"+str(ga.number))
               if int(fl.number)!=int(amountFlights) or int(bay.number)!=int(amountBays) or i+1!=len(bay.linkedGates):
                  f.write(" + ") 
               else:
                  f.write("")
                   
    f.write("\n")
    f.write("\n")

    #generate constraints
    f.write("Subject to:\n")
        
    #Have all flights require a bay for full stay
    for fl in Flight._registry:
        for bay in Bay._registry:
            curVar=str("X_I"+str(fl.number)+"_K"+str(bay.number))
            f.write(curVar)
            if int(bay.number)!=int(amountBays):
                f.write(" + ") 
            else:
                f.write(" = 1 \n")     
                
#    #Have all flights require a gate
    for fl in Flight._registry:
        for ga in Gate._registry:
            curVar=str("X_I"+str(fl.number)+"_L"+str(ga.number))
            f.write(curVar)
            if int(ga.number)!=int(amountGates):
                f.write(" + ") 
            else:
                f.write(" = 1 \n")                  
                
    #Link X_I_K_L with X_I_K and X_I_L
    for fl in Flight._registry: #X_I
        for bay in Bay._registry:  #X_I_L        
            for i in range(len(bay.linkedGates)): 
                ga=bay.linkedGates[i]
                curXIKL=str("X_I"+str(fl.number)+"_K"+str(bay.number)+"_L"+str(ga.number))
                curXIK=str("X_I"+str(fl.number)+"_K"+str(bay.number))
                curXIL=str("X_I"+str(fl.number)+"_L"+str(ga.number))
#               Either or constraints, as is depicted in slides.    
#               x1 must be 1 for x2 to be 1 
#               -x1+x2<=0
#               x1+x2-y1<=1                
                
#               XIK must be 1 for XIKL to be 1
                f.write("-"+curXIK+" + "+curXIKL+" <=0\n") #both zero
                f.write( curXIKL+" + "+curXIK+ " - " + curXIKL+"_Y"+ " <=1\n") # both 1, _Y = 1
                
#               XIL must be 1 for XIKL to be 1
                f.write("-"+curXIL+" + "+curXIKL+" <=0\n")
                f.write( curXIKL+" +"+curXIL+"-" + curXIKL+"_Y"+ " <=1\n")
                
    #Have all flights require an XIKL (bay and gate)
    for fl in Flight._registry:
        for bay in Bay._registry:           
            curXIK=str("X_I"+str(fl.number)+"_K"+str(bay.number))
            for i in range(len(bay.linkedGates)):
                ga=bay.linkedGates[i]
                curXIL=str("X_I"+str(fl.number)+"_L"+str(ga.number))                    
                curXIKL=str("X_I"+str(fl.number)+"_K"+str(bay.number)+"_L"+str(ga.number))
                
#               Sum of all XIKL for this flight = 1                
                f.write(curXIKL)
                if i != len(bay.linkedGates)-1:
                    f.write(" + ")
            if bay.number != amountBays: 
                f.write(" + ")
        f.write("= 1 \n")      
    
    #Time overlap constraint:        
    #For all overlapping flights, bays can only have one flight assigned:
    for i in range(len(timemat)):
        for j in range(i):
            if timemat[i,j]==1:
                flight1=Flight._registry[i]
                flight2=Flight._registry[j]
                for bay in Bay._registry:
                    flight1var=str("X_I"+str(flight1.number)+"_K"+str(bay.number))
                    flight2var=str("X_I"+str(flight2.number)+"_K"+str(bay.number))
                    f.write(flight1var + " + " + flight2var + " <= 1 \n") 
                    
    #Time overlap constraint: For gates.                    
    for i in range(len(timemat)):
        for j in range(i):
            if timematArr[i,j]==1:
                flight1=Flight._registry[i]
                flight2=Flight._registry[j]
                for gate in Gate._registry:
                    flight1var=str("X_I"+str(flight1.number)+"_L"+str(gate.number))
                    flight2var=str("X_I"+str(flight2.number)+"_L"+str(gate.number))
                    f.write(flight1var + " + " + flight2var + " <= 1 \n") 
            if timematDep[i,j]==1:
                flight1=Flight._registry[i]
                flight2=Flight._registry[j]
                for gate in Gate._registry:
                    flight1var=str("X_I"+str(flight1.number)+"_L"+str(gate.number))
                    flight2var=str("X_I"+str(flight2.number)+"_L"+str(gate.number))
                    f.write(flight1var + " + " + flight2var + " <= 1 \n") 
                
    #Gate constrain 1: # domestic flights to domestic gates, vice versa
    #Domestic flights at domestic gates
    #Sum of domestic gates per domestic flight = 1. 
    for fl in Flight._registry:
        if fl.domestic == True:
            for ga in Gate._registry:
                if ga.domesticGate == True:
                    curVar = str("X_I"+str(fl.number)+"_L"+str(ga.number))
                    if ga.number == Gate.finalDomesticNumber:
                        f.write(curVar + " = 1 \n")
                    else:
                        f.write(curVar + " + ")
    #International flights not at domestic gates
    #Sum of domestic gates per international flight = 0
    for fl in Flight._registry:
        if fl.domestic == False:
            for ga in Gate._registry:
                if ga.domesticGate == True:
                    curVar = str("X_I" + str(fl.number) + "_L" + str(ga.number))
                    if ga.number == Gate.finalDomesticNumber:
                        f.write(curVar + " = 0 \n")
                    else:
                        f.write(curVar + " + ")

    #Gate constrain 2: # ensures flights after 8 pm are not in gates closed after that hour
    for fl in Flight._registry:
        if fl.timeSlotEnd >= timeTo5Min("8pm"):
            for ga in Gate._registry:
                if ga.terminal.openEvening==False:
                    flight1var = str("X_I"+str(fl.number) + "_L" + str(ga.number))
                    if ga.number == Gate.finalEveningClosedNumber:
                        f.write(flight1var + " = 0 \n")                        
                    else:
                        f.write(flight1var + " + ")
                        
#    #Bay constraint 2: or Form factor constraint: (Compliance of a/c formfactor to bay/gate)
    FF_all = []
    FF_compliance1 = []
    FF_compliance2 = []
    for bay in Bay._registry:
        if bay.formFactor not in FF_all:
            FF_all.append(bay.formFactor)
            
    for i in range(len(FF_all)): 
        lst = []
        for bay in Bay._registry:
            if bay.formFactor == FF_all[i]:
                lst.append(bay.number)
        temp1 = list(lst)
        FF_compliance1.append(temp1)
  
    stored_list = []
    for i in range(len(FF_compliance1)):
        if i == 0:
            templist1 = []
            for j in FF_compliance1[i]:
                templist1.append(j)
                stored_list.append(j)
            FF_compliance2.append(templist1)
        else:
            templist1 = []
            for j in FF_compliance1[i]:
                templist1.append(j) 
            stored_list.extend(templist1)
            newlist = sorted(stored_list)
            FF_compliance2.append(newlist)

    for fl in Flight._registry:
        for bay in Bay._registry:
            for i in range(len(FF_all)):
                for j in range(len(FF_compliance2[i])):
                    if fl.formFactor == FF_all[i] and bay.number==FF_compliance2[i][j]:
                        f.write("X_I"+str(fl.number)+"_K"+str(bay.number))
                        if int (bay.number) == FF_compliance2[i][-1]:
                            f.write(" = 1 \n")
                        if int(bay.number) != FF_compliance2[i][-1]:
                            f.write(" + ")
    f.write("\n")
    #Make parameters binary as needed
    
    #Bay constraint 4: Refueling constraint 
    for fl in Flight._registry:
        if fl.needToRefuel == True:
            for bay in Bay._registry:
                if bay.refuelBay == True:
                    f.write("X_I"+str(fl.number)+"_K"+str(bay.number))
                    if bay.number == bay.finalRefuelBay:
                        f.write(" = 1 \n")
                    else: 
                        f.write(" + ")
    maxj=80                            
    f.write("binary\n")
    j=0
    for i in binlist:
        f.write(i+" ")
        j+=1
        if j == maxj:
            f.write("\n")
            j = j-maxj
    #write end file
    f.write("\n")
    f.write("end")


#RUN CPlex:
sol = generateRunFiles("SecondIteration.lp")   #Returns solution filepath

lines = [line.rstrip('\n') for line in open(sol)]
lines = [line.strip() for line in lines]

if lines[6].split('=')[0]=='objectiveValue':
    objectiveValue=float(lines[6].split('=')[1].strip('"'))
    print("CPLEX objective value is",objectiveValue)
else:
    print("ERROR: objectiveValue not at expected location!")

#Import data:
tree = ET.parse(sol)
root = tree.getroot()

solNameList=[]
solValueList=[]
for child in root[3]:
    locals().update(child.attrib) #name,value,index
    solNameList.append(name)
    solValueList.append(value)


#retrieve X_I_L, X_I_K from solution, send to objects
a = np.zeros((amountFlights,amountGates))
b = np.empty((amountFlights,amountGates), dtype=object)        
c = np.zeros((amountFlights,amountBays))
d = np.empty((amountFlights,amountBays), dtype=object)  
      
for fl in Flight._registry:
    for ga in Gate._registry:
        i = fl.number-1
        j = ga.number-1
        curVar=str("X_I"+str(fl.number)+"_L"+str(ga.number))
        findVar=solNameList.index(curVar)
        a[i,j]=solValueList[findVar]
        b[i,j]=solNameList[findVar]
        if 0.999999 <= float(solValueList[findVar]) <= 1.0001:
            fl.assignGate(ga)
            
    for bay in Bay._registry:
        i = fl.number-1
        j = bay.number-1
        curVar=str("X_I"+str(fl.number)+"_K"+str(bay.number))
        findVar=solNameList.index(curVar)
        c[i,j]=solValueList[findVar]
        d[i,j]=solNameList[findVar]
        if 0.999999 <= float(solValueList[findVar]) <= 1.0001:
            fl.assignBay(bay)

#retrieve objective functions:
obj1=0
for fl in Flight._registry:
    for ga in Gate._registry:
       mult = fl.passengers*ga.distanceToTerminal
       curVar = "X_I"+str(fl.number)+"_L"+str(ga.number)
       findVar = solNameList.index(curVar)
       obj1 += float(solValueList[findVar]) * mult

obj2=0
for fl in Flight._registry: #Z2 = sum_i sum_k Xi,k * Dterm_k
    for ga in Gate._registry:
       if int(fl.gatePref)==ga.number:
           curVar = "X_I"+str(fl.number)+"_L"+str(ga.number)
           findVar=solNameList.index(curVar)
           obj2 += -float(solValueList[findVar])

obj3=0
weight=2
for fl in Flight._registry:
    for bay in Bay._registry:
       for i in range(len(bay.linkedGates)):
           ga=bay.linkedGates[i]
           gaDist=bay.linkedGatesDistances[i] 
           mult = fl.passengers*gaDist
           curVar = "X_I"+str(fl.number)+"_K"+str(bay.number)+"_L"+str(ga.number)
           findVar=solNameList.index(curVar)
           obj3 += float(solValueList[findVar]) * mult * weight

print("Objective function for gate to terminal distance (obj1):  ",obj1)
print("Objective function for gate preference (obj2):  ",obj2)
print("Objective function for gate to bay distance (obj3):  ",obj3)
print("Objective function 1 and 3 combined: ", obj1+obj3)


#Grafiekje solution:
if plotResults == 1:
    t=['12am','1am','2am', '3am', '4am', '5am', '6am', '7am', '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm', '12am']
    tTo5Min = []
    for i in range(len(t)):
        tTo5Min.append(timeTo5Min(t[i]))
    tStartIndex = tTo5Min.index(timeTo5Min(plotTimeStart))
    tEndIndex   = tTo5Min.index(timeTo5Min(plotTimeEnd))    
    #getTimetableMatrix(timeStart,timeEnd,amountGates)
    timetableMatrix=getTimetableMatrixGates(t[tStartIndex],t[tEndIndex],amountGates)
    timetableMatrix2=getTimetableMatrixBays(t[tStartIndex],t[tEndIndex],amountBays,1)
    #plotTimeTable
    plotTimetableGates(timetableMatrix,1,xTickLabels=t[tStartIndex:tEndIndex+1],xTickSpacing=11,yTickLabels=True)
    plotTimetableBays(timetableMatrix2,1,xTickLabels=t[tStartIndex:tEndIndex+1],xTickSpacing=11,yTickLabels=True,bays=1)

#Bonus:
#e.g. 20 min on departure and 10 on arrival for gate, full time for bay.

todo("Eventueel towing implementen (Naar andere bay als dat goedkoper is)")
todo("Eventueel een A bay bezetbaar maken door 2 C planes")
#
#obj1List.append(-obj1)
#obj2List.append(-obj2)
#obj3List.append(-obj3)
#objectiveList.append(objectiveValue)