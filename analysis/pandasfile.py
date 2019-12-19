# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:48:31 2019

@author:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=pd.Series(np.random.randn(5),index=['a','b','c','d','e']) #randn generates -1 to 1 while random generates 0 to 1
print(a)
print(a.index)

d={"b":1,"a":0,"c":2}
b=pd.Series(d)
print(b)

a=[2,1,4,3,5,4,6]
fun=np.exp(a)
print(fun)
print(a[1:])
print(a[:-1])

#------------------------------------------------------------

mydata=pd.read_table("http://bit.ly/chiporders",sep="\t")
mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.head())
print(mymoviedata.tail())
print(mymoviedata.iloc[:,1])
print(mymoviedata.iloc[10:21,:])
data1=mydata[["item_name","quantity"]]
data2=mydata.iloc[:,1:3]
plt.plot(data1["item_name"],data1["quantity"])
print(mydata["order_id"].std())
print(mydata["order_id"].mean())
print(mydata["order_id"].sum())

data1.to_csv("data1.csv")

print("mean :",mydata.mean())
print("Description :",mydata.describe())
print(data1.max())
print(data1.corr())
print(data1.median())
print(data1.std())
print(data1.count())



mydata["mycnt"]=mydata["item_price"].map(lambda x:len(x))
print(mydata)
df1=mydata.loc[(mydata["item_name"]=="chicken Bowl"),["order_id","quantity"]==""]


