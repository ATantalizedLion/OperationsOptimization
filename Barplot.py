# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

obj1List = [1392880.0, 1392880.0, 1404620.0, 1392880.0, 1404620.0, 1406240.0, 1471640.0, 1476420.0, 1392880.0, 1423480.0, 1392880.0, 1392880.0] 
obj2List = [-2.0, -2.0, -3.0, -2.0, -3.0, -4.0, -4.0, -3.0, -3.0, -3.0, -3.0, -3.0] 
obj3List = [1720200.0, 1720200.0, 1720200.0, 1720200.0, 1720200.0, 1903600.0, 1893200.0, 1699500.0, 1720200.0, 1720200.0, 1720200.0, 1720200.0] 
obj4List = [4833280.0, 4833280.0, 4845020.0, 4833280.0, 4845020.0, 5213440.0, 5258040.0, 4875420.0, 4833280.0, 4863880.0, 4833280.0, 4833280.0]
a = obj2List

c=a[0] #correction factor
b=[]
d=[]
e=[]
for i in range(len(a)):
    b.append(a[i]-c)
    if i == 0:
        d.append("No Gate")
    elif i%2 == 0:
        d.append("Gate " + str(i))
    else:
        d.append("")
    e.append(i)
x=range(13)

plt.bar(x,a)
plt.title("Objective function as function of KLM gate preference")
plt.xticks(e,d)
plt.ylabel("Objective function value")
plt.xlabel("Gate")
plt.show()

#
#generated with 
#
#Flight('BML1', 297, '20:45', '21:55', 'B', Airline._registry[3], domestic=False)
#Flight('SYD2', 387, '15:30', '17:00', 'A', Airline._registry[0], domestic=False)
#Flight('BRU3', 221, '16:05', '17:35', 'B', Airline._registry[3], domestic=False)
#Flight('BRU4', 270, '22:20', '23:05', 'B', Airline._registry[2], domestic=False)
#Flight('BLN5', 329, '18:10', '19:35', 'A', Airline._registry[3], domestic=False)
#Flight('BLN6', 180, '16:50', '17:40', 'B', Airline._registry[5], domestic=False)
#Flight('ROM7', 381, '22:10', '23:20', 'A', Airline._registry[4], domestic=False)
#Flight('BRU8', 97, '17:25', '18:35', 'C', Airline._registry[2], domestic=False)
#Flight('SYD9', 358, '19:40', '20:45', 'A', Airline._registry[2], domestic=False)
#Flight('BRU10', 88, '15:45', '17:15', 'C', Airline._registry[3], domestic=False)
#Flight('BML11', 175, '19:10', '20:35', 'B', Airline._registry[4], domestic=False)
#Flight('NYC12', 345, '15:30', '17:10', 'A', Airline._registry[4], domestic=False)
#Flight('PAR13', 182, '22:45', '24:30', 'B', Airline._registry[5], domestic=False)
#Flight('AMS14', 214, '19:10', '21:10', 'B', Airline._registry[5], domestic=True)
#Flight('BRU15', 102, '20:20', '22:05', 'C', Airline._registry[1], domestic=False)
#Flight('SYD16', 360, '18:50', '20:50', 'A', Airline._registry[2], domestic=False)
#Flight('PAR17', 126, '21:00', '22:45', 'C', Airline._registry[2], domestic=False)
#Flight('PAR18', 173, '15:15', '16:00', 'B', Airline._registry[1], domestic=False)
#Flight('ROM19', 309, '16:15', '18:10', 'A', Airline._registry[3], domestic=False)
#Flight('AMS20', 150, '15:50', '16:45', 'B', Airline._registry[5], domestic=True)
#Flight('LON21', 405, '15:50', '17:15', 'A', Airline._registry[0], domestic=False)
#Flight('PAR22', 104, '21:40', '23:25', 'C', Airline._registry[5], domestic=False)
#Flight('LEY23', 113, '20:05', '21:55', 'C', Airline._registry[3], domestic=True)
#Flight('LEY24', 125, '22:50', '24:35', 'C', Airline._registry[4], domestic=True)
#Flight('NYC25', 375, '19:15', '20:05', 'A', Airline._registry[3], domestic=False)
#Flight('LEY26', 57, '20:45', '22:30', 'C', Airline._registry[2], domestic=True)
#Flight('BML27', 284, '20:10', '20:55', 'B', Airline._registry[5], domestic=False)
#Flight('ROM28', 262, '15:30', '16:25', 'B', Airline._registry[1], domestic=False)
#Flight('BRU29', 221, '21:30', '22:15', 'B', Airline._registry[5], domestic=False)
#Flight('NYC30', 360, '15:25', '16:40', 'A', Airline._registry[5], domestic=False)
##Bru15
##Par18
##Rom28