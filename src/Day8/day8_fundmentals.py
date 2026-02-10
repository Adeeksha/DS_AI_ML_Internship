# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 10:38:08 2026

@author: ADEEKSHA
"""

#Code Example
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
print(b)
print()
c = np.array([[40,50,60],[5,9,8],[7,4,5]])
print(c)
print()
d=np.array([])
print(d)
print()

result = a + b
print(result)
print()

#vectorized vs Loop example
arr=np.random.rand(1000000)
print(arr)
print()

#vectorized
squared=arr**2
print(squared)
print()
arr2=np.random.randint(100)
print(arr2)
print()
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)
print()
a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)
print()
hstacked = np.hstack((a,b))
print(hstacked)
print()

data=np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))
print(np.mean(data,axis=1))
print()

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

print()
arr=np.linspace(0,2,5)
print(arr)
print()
arr=np.linspace(0,3,4)
print(arr)
