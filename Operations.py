# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:21:08 2019

@author: Daan
"""

from math import *
import numpy as np
from OOFunc import generateRunFiles,timeToMin,timeTo5Min


#Can also combine these into an array similar to the one for flights, would keep it overzichtelijker
gates = ["1","2","3","4"] #change to numbers or anything if you prefer
gatesDOM = [True, True, False, False] #Is the gate domestic?
gatesClosedEvening = [] #Is the gate closed in the evening?

#Name, identifier/number, Passengers Pi, Arrival time, Departure time, form factor, airliner(?) (For gate/terminal preference!)
flight1 = ["JFK23", 1, 250, timeTo5Min("5pm"),timeTo5Min("7pm")+2,"A","KLM"]
flight2 = ["JFK23", 2, 250, timeTo5Min("5pm"),timeTo5Min("7pm"),"B","Easyjet"]
flights = np.array([flight1,flight2])

print("Update dataset") #Boris

#add buffers (10 min)
print("Implement buffers") #Boris

print("Implement Generate Time Matrix") #Boris

#list for binary generation
binlist=[]

#Take input flights and generate LP file
f = open("LPFiles\FirstIteration.lp","w+")    

#generate Objective
f.write("Maximize objective:\n")
f.write("X_1+2X_2\n") #OBJECTIVE NEEDS TO BE CHANGED OBVIOUSLY
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
for i in range(len(flights)):
    for j in range(len(gates)):
        curVar=str("X_I"+flights[i][1]+"_L"+gates[j])
        if gatesDOM[j] == True:
            f.write(curVar+"\n")
        else:
            f.write(curVar+"\n")            
        binlist.append(curVar)

#Gate constrain 2: 
print("Implement GC2") #Daan

#Form factor constriant: (Compliance of a/c formfactor to bay/gate) 
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


