# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:21:08 2019

@author: Daan
"""

from math import *
import numpy as np


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
    return int(converted/5)



#    Name, identifier/number, Passengers Pi, Arrival time, Departure time, form factor
flight1 = ["JFK23", 1, 250, timeTo5Min("5pm"),timeTo5Min("7pm")+2,"A"]
flight2 = ["JFK23", 2, 250, timeTo5Min("5pm"),timeTo5Min("7pm"),"B"]
flights = np.array([flight1,flight2])

print("Update dataset") #Boris

#add buffers (10 min)
print("Implement buffers") #Boris


#list for binary generation
binlist=[]

#Take input flights and generate LP file
f = open("FirstIteration.lp","w+")    

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

#Gate constraint 1: Domestic flight to dom gate
print("Implement GC1") #Daan

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




#Show dataset
print("Implement dataset mooie grafiekjes") #Boris

#Show solution
print("Implement solution mooie grafiekjes")



#Bussen bij gate X, als bus er is, telt afstand minder zwaar
print("Implement showoff")


