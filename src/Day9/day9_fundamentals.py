# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:29:28 2026

@author: ADEEKSHA
"""

import pandas as pd
s1=pd.Series([10,20,30,40])
s2=pd.Series([10,20,30],index=['a','b','c'])

print(s1)
print(s2)
print()
#indexing
marks=pd.Series([85,90,78],index=['Math','Physics','Chemistry'])
print(marks['Math'])
print(marks[['Math','Chemistry']])
print()
#Boolean Masking
scores=pd.Series([45,67,89,34,90])
passed=scores[scores>60]
print(passed)
print()
#handling missing data
data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(0))

print()

data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(3))

print()

#vectorized string operations
names=pd.Series(['Alice', 'bob', 'CHARLIE','alien'])

print(names.str.lower())
print(names.str.contains('a'))