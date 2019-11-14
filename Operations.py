# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:21:08 2019

@author: Daan
"""

from math import *
import numpy as np



#Where to start...





#generate LP file

    #generate Objective, constraints
    
    #Make parameters binary as needed

    #Write everything to LP file



#=================================================
            # Test for writing lp files
#=================================================
f = open("Test.lp","w+")
f.write("max: X_1+2*X_2;\n\n")
f.write("C1: X_1<=12;\n")
f.write("C2: X_2<=13;\n")
f.close() #Works in LP Solve!

    
#Write everything to file
f = open("TestCPlex.lp","w+")
f.write("Maximize objective:\n")
f.write("X_1+2X_2\n
f.write("\n")
f.write("Subject to:\n")
f.write("X_1<=12\n")
f.write("X_2<=13\n")
f.write("\n")
f.write("End\n")
f.close() #works in CPLex, probably
    
    