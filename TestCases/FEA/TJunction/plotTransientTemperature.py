# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:03:09 2016

@author: makke
"""

import FreeCAD
import Plot
import numpy as np
plt=Plot.matplotlib.pyplot
 

#Get list of anylysis memebers
members=FreeCAD.ActiveDocument.MechanicalAnalysis.Member

time=[]
yvalue=[]
#value=[]
for member in members:
     if member.isDerivedFrom("Fem::FemResultObject"):
        memresult=member
        #Check first object and toggle visibility to oppesite 
#        P1=np.array(memresult.PrincipalMax)
#        P2=np.array(memresult.PrincipalMed)
#        P3=np.array(memresult.PrincipalMin)
        Von=np.array(memresult.StressValues)
#        T=np.array(memresult.Temperature)
#        dispvectors=np.array(memresult.DisplacementVectors)
#        x=np.array(dispvectors[:, 0])
#        y=np.array(dispvectors[:, 1])
#        z=np.array(dispvectors[:, 2])
        #Print messages for testing
        #FreeCAD.Console.PrintMessage(str(member.Name)+" \n")
        #FreeCAD.Console.PrintMessage(str(member.Time)+" \n")
        #Save the value you need 
        time.append(member.Time)
        yvalue.append(max(Von))
#        yvalue.append(max(T))
        
        
# plot with various axes scales
plt.figure(1)
plt.plot(time,yvalue)
#plt.plot(time,value)
plt.title('Max Von Mises vs time')
plt.xlabel('Time (S)')
plt.ylabel('Max Von Mises (MPa)')
plt.grid(True)
plt.show()