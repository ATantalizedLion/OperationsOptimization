# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:27:18 2019

@author: Daan
"""
#Functions for Operation Optimization

from os import getcwd,remove

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
    converted=timeToMin(Time)
    return int(converted/5)

def generateRunFiles(lpFileName):
    #lpFileName is the name of the LP file (without.lp) in the LPFiles directory in the current work directory
    lpFileName=lpFileName.strip(".lp")
    filepath=getcwd()+"\LPFiles"
    CCFPath=filepath+"\\"+lpFileName+"CCF.CCF"
    BatPath=filepath+"\\"+lpFileName+"Run.bat"
    SOLPath=filepath+"\\"+lpFileName+"SOL.SOL"
    LpPath=filepath+"\\"+lpFileName+".lp"
    #generate CCF:
    f = open(CCFPath,"w+")
    f.write("read "+LpPath+"\n")
    f.write("opt\n")
    f.write("write "+SOLPath+"\n")
    f.write("quit\n")
    f.close() 
    #generate BAT
    f = open(BatPath,"w+")
    f.write('"C:\Program Files\IBM\ILOG\CPLEX_Studio129\cplex\\bin\\x64_win64\cplex.exe" < '+CCFPath)
    f.close() 
    #run BAT
    from subprocess import Popen
    p = Popen(BatPath)
    p.wait()
    #cleanUpCCFandBAT:
    remove(BatPath)
    remove(CCFPath)
    return