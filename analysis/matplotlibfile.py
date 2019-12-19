# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:16:35 2019

@author: 
"""

import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
x2=[1,2,3]
y2=[10,13,14]
plt.plot(x,y,label="first line")
plt.plot(x2,y2,label="second line")
plt.xlabel("plot number")
plt.ylabel("important var")
plt.legend()
plt.grid()
plt.title("this is my first matplot graph")
plt.show()
#-----------------------------------------------------------------------------------------

slices=[1,6,3,13,1]
activities=["exercise","sleeping","eating","studying","time-wasted"]
cols=["c","m","r","g","k"]

plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0.2,0,0,0))
plt.title("CDAC students time-table")
plt.show()
#-----------------------------------------------------------------------------------------
Dayofweekofcall=[1,2,3]
Dispactchesonthisweekday=[77,32,42]
Labels=["monday","tuesday","wednesday"]
plt.bar(Dayofweekofcall,Dispactchesonthisweekday,align="center")
plt.xticks(Dayofweekofcall,Labels,rotation="45")
plt.show()
#--------------------------------------------------------------------------------------------------

plt.plot([],[],color="m",label="sleeping  ")

