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

#bad data (double mult on obj3), fix:
for i in range(len(obj3List)):
    obj3List[i] = obj3List[i]/2
    obj4List[i] = int(2*obj3List[i]+obj1List[i])

a = obj2List
c=a[0] #correction factor
b=[]
d=[]
e=[]
for i in range(len(a)):
    b.append(-a[i])
    if i == 0:
        d.append("No Gate")
    elif i%2 == 0:
        d.append("Gate " + str(i))
    else:
        d.append("")
    e.append(i)

f=obj4List #bar_labels


fig,ax = plt.subplots()

bar_plot = plt.bar(e,b)

for idx,rect in enumerate(bar_plot):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
            f[idx],
            ha='center', va='bottom', rotation=90)

plt.title("Objective functions as function of KLM gate preference")
plt.xticks(e,d)

plt.ylabel("Objective function 2 value")
plt.xlabel("Total objective value inside bar")

plt.show()

