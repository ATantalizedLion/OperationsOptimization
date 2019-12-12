# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

obj1List=[-1547020.0,
 -1547020.0,
 -1547020.0,
 -1547020.0,
 -1547020.0,
 -1589220.0,
 -1591580.0,
 -1625780.0,
 -1589220.0,
 -1547020.0,
 -1577620.0,
 -1547020.0,
 -1550680.0]

obj2List= [2.0, 2.0, 3.0, 2.0, 3.0, 3.0, 4.0, 4.0, 3.0, 3.0, 3.0, 3.0, 3.0]

obj3List= [-826650.0,
 -826650.0,
 -826650.0,
 -826650.0,
 -826650.0,
 -826650.0,
 -913150.0,
 -913150.0,
 -826650.0,
 -826650.0,
 -826650.0,
 -826650.0,
 -826650.0]

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

plt.bar(x,b)
plt.title("Change in objective function as function of KLM gate preference")
plt.xticks(e,d)
plt.ylabel("Change in objective function (from no gate)")
plt.xlabel("Gate")
plt.show()
