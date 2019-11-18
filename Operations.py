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

#    Name, identifier/number, Passengers Pi, Arrival time, Departure time, form factor
flight1 = ["JFK23", 1, 250, timeToMin("5pm"),timeToMin("7pm"),"A"]
flight2 = ["JFK23", 2, 250, timeToMin("5pm"),timeToMin("7pm"),"B"]
flights = np.array([flight1,flight2])




#list for binary generation
binlist=[]

#Take input flights and generate LP file
f = open("Firstiteration.lp","w+")    

#generate Objective
f.write("Maximize objective:\n")
f.write("X_1+2X_2\n") #OBJECTIVE NEEDS TO BE CHANGED OBVIOUSLY
f.write("\n")    

#generate constraints
f.write("Subject to:\n")
for i in range(len(flights)):
    f.write("X_"+flights[i][1]+"....\n")
    binlist.append("X_"+flights[i][1])

f.write("\n")
#Make parameters binary as needed
f.write("binary\n")

for i in binlist:
    f.write(i+" ")

#write end file
f.write("\n")
f.write("end")
