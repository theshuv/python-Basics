# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:27:14 2019

@author: dbda24
"""
import pandas as pd
dummy_data1={"id":["1","2","3","4","5"],"feature1":["A","C","E","G","I"],
            "feature2":["B","D","F","H","J"]}
df1=pd.DataFrame(dummy_data1,columns=["id","feature1","feature2"])


dummy_data2={"id":["1","2","6","7","8"],"feature1":["K","M","O","Q","S"],
            "feature2":["L","N","P","R","T"]}
df2=pd.DataFrame(dummy_data2,columns=["id","feature1","feature2"])

df3=pd.concat([df1,df2],ignore_index=True)


print(df1)
print(df2)
print(df3)

dummy_data3={"id":["1","2","6","7","8"],"feature1":["K","M","O","Q","S"],
            "feature2":["L","N","P","R","T"]}
df3=pd.DataFrame(dummy_data3,columns=["id","feature3"])
df4=pd.merge(df1,df3,on="id")
print(df4)