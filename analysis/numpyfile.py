# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:05:18 2019

@author: dbda24
"""

import numpy as np
a=np.array([1,2,3,4,5.2],dtype=complex)
print(a)
print(a.dtype)
a=np.ones((2,3,4),dtype=int)
print(a)
z=np.zeros((3,4))
print(z)
e=np.empty((3,4))
print(e)

s=np.arange(24).reshape(2,3,4)
print(s)


q=np.array([20,30,40,50])
w=np.arange(4)
print(q)
print(w)
r=q-w
print(r)
t=w**2                    #squaring of numbers in array
print(t)

y=np.sin(w)               #finding sin of numbers in array
print(y)

u=q.dot(w)           #matrix multiplication
print(u)

o=np.ones((2,3),dtype=int)
i=np.random.random((2,3))           #random value generation
o*=3                           #multiplying o array elements by 3
print(o)
i+=o                   #adding i array elements with o array elements and storing in i.
print(i)

