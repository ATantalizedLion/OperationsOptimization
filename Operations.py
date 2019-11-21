# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:21:08 2019

@author: Daan
"""

import matplotlib.pyplot as plt
from OOFunc import generateRunFiles,Flight,Airline,Gate,Terminal,timeToMin

#Terminal(name,openEvening,distance)
t1 = Terminal("A",True,600)

#Gate(terminal,domesticFlight,distanceToTerminal)
g1 = Gate(t1,True,500)
g2 = Gate(t1,True,600)
g3 = Gate(t1,True,600)
g4 = Gate(t1,True,600)
g5 = Gate(t1,True,600)
g6 = Gate(t1,True,600)
g7 = Gate(t1,True,600)
g8 = Gate(t1,True,600)
g9 = Gate(t1,True,600)
g10 = Gate(t1,True,600)

#Airliner(name,gatePref)
AirFrance   = Airline("AirFrance",g3)
Delta = Airline("Delta",g4)
BritishAirways=Airline("British Airways",g5)
Transavia=Airline("Transavia",g6 )
EasyJet = Airline("EasyJet",g7)
KLM = Airline("KLM",g8)

#Flight(identifier,passengers,arrivalTime,departureTime,formFactor,airliner)
fl1 = Flight("JFK23", 250, "5:15pm","7pm","A",KLM)
fl2 = Flight("JFK24", 255, "5:25pm","6:35pm","B",EasyJet)
fl3 = Flight("JFK26", 255, "5:55pm", "7:05pm","C",Delta)
fl4 = Flight("JFK27", 255, "6:05pm", "7:10pm","D",BritishAirways)
fl5 = Flight("JFK28", 255, "6:15pm", "7:15pm","A",Transavia)
fl6 = Flight("JFK29", 255, "6:25pm", "7:20pm","D",Transavia)
fl7 = Flight("JFK30", 255, "6:30pm", "7:30pm","C",AirFrance)
fl8 = Flight("JFK31", 255, "6:35pm", "7:45pm","A",Transavia)
fl9 = Flight("JFK32", 255, "6:50pm", "8:10pm","B",KLM)
f20 = Flight("JFK33", 255, "6:50pm", "8:25pm","D",KLM)
f21 = Flight("JFK34", 255, "7:05pm", "8:45pm","B",KLM)
f22 = Flight("JFK35", 255, "7:15pm", "8:55pm","C",KLM)
f23 = Flight("JFK36", 255, "7:30pm", "9:05pm","A",Transavia)
f24 = Flight("JFK37", 255, "7:45pm", "9:20pm","C",BritishAirways)
f25 = Flight("JFK38", 255, "8:15pm", "10:05pm","B",EasyJet)


print("Update dataset") #Boris

print("Implement Generate Time Matrix") #Boris

#list for binary generation
binlist=[]

#Take input flights and generate LP file
f = open("LPFiles\FirstIteration.lp","w+")    

P = [['P1',100],['P2',200]]
D = [['D11',1],['D12',1]]
X = ['X_I1_L1','X_I1_L2']
PREF = [['PREF11',3],['PREF12',2]]





#generate Objective
f.write("Minimize multi-objective:\n") #Z1 = sum_i sum_k Pi*Xi,k*Dterm_k
f.write("OBJ1: \n")

for fl in Flight._registry:
    for ga in Gate._registry:
       f.write(str(fl.passengers))
       f.write("X_I"+str(fl.number)+"_L"+str(ga.number))
       f.write(str(ga.distance)) 
       f.write("+")
f.write("\n")
f.write("\n")
f.write("OBJ2: \n")
for fl in Flight._registry: #Z2 = sum_i sum_k Xi,k * Dterm_k
    for ga in Gate._registry:
       f.write("-"+"X_I"+str(fl.number)+"_L"+str(ga.number))
f.write("\n")
f.write("\n")
print("Implement objectives") #Tommy

#generate constraints
f.write("Subject to:\n")

# Example for loop for constraints
#for i in range(len(flights)):
#    f.write("X_"+flights[i][1]+"....\n")
#    binlist.append("X_"+flights[i][1])

#Time overlap constraint:
print("Implement Time overlap constraint") #Daan - After matrices by boris are done
print("Implement GC1") #Daan #Gate constraint 1: Domestic flight to dom gate
print("Think I need time matrix here. Otherwise I'm summing all flights.")

for fl in Flight._registry:
    for ga in Gate._registry:
        curVar=str("X_I"+str(fl.number)+"_L"+str(ga.number))
        if ga.domesticFlight == True:
            f.write(curVar+"\n") #IMPLEMENT
        else: 
            f.write(curVar+"\n") #IMPLEMENT 
        binlist.append(curVar) #Make binary

#Gate constrain 2: # ensures flights after 6 pm are not in B or C 
print("Implement GC2") #Daan

#Form factor constraint: (Compliance of a/c formfactor to bay/gate) 
print("Implement FFC") #Tommy

f.write("\n")
#Make parameters binary as needed
f.write("binary\n")
for i in binlist:
    f.write(i+" ")
#write end file
f.write("\n")
f.write("end")
f.close

#RUN CPlex
print("Running CPlex")
generateRunFiles("FirstIteration.lp")
print("CPlex should be done.")


#Show dataset
print("Implement dataset mooie grafiekjes") #Boris



#Show solution
print("Implement solution mooie grafiekjes")



#Bussen bij gate X, als bus er is, telt afstand minder zwaar
print("Implement showoff")


