# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:21:08 2019

@author: Daan
"""

import matplotlib.pyplot as plt
from OOFunc import generateRunFiles,Flight,Gate,Terminal,timeToMin

#Terminal(name,openEvening,distance)
t1 = Terminal("A",True,600)

#Gate(terminal,domesticFlight,distanceToTerminal)
g1 = Gate(t1,True,500)

#Flight(identifier,passengers,arrivalTime,departureTime,formFactor,airliner)
fl1 = Flight("JFK23", 250, "5pm","7pm","A","KLM") 
fl2 = Flight("JFK24", 255, "5pm","7pm","B","EasyJet")
fl3 = Flight("JFK25", 255, "6pm", "8pm","A","Airfrance")

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
f.write("Minimize objective:\n") #Z1 = sum_i sum_k Pi*Xi,k*Dterm_k
for i in range(len(X)):
    for j in range(len(D)):
       f.write(P[i][0])
       f.write("*")
       f.write(X[i])
       f.write("*")
       f.write(D[j][0]) 
       if i==(len(X)-1) and j==(len(D)-1):
           f.write("")
       else:
           f.write("+")
f.write("\n")
f.write("\n")

f.write("Maximize objective:\n") #Z2 = sum_i sum_k Xi,k * Dterm_k
for i in range(len(X)):
    for j in range(len(D)):
       f.write(X[i])
       f.write("*")
       f.write(PREF[j][0]) 
       if i==(len(X)-1) and j==(len(D)-1):
           f.write("")
       else:
           f.write("+")
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
        curVar=str("X_I"+fl.number+"_L"+ga.name)
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


