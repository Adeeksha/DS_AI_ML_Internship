# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:02:50 2026

@author: ADEEKSHA
"""

import pandas as pd
products=pd.Series([700,150,300],index=['Laptop','Mouse','Keyboard'])
laptop_price=products['Laptop']
first_two=products[:2]
print("Full Series:")
print(products)
print("\nPrice of Laptop:")
print(laptop_price)
print("\nFirst Two Products (Positional Indexing):")
print(first_two)