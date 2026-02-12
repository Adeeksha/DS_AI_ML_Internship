# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:56:58 2026

@author: ADEEKSHA
"""

import pandas as pd
df = pd.read_csv("location_dirty_data.csv")
print(df["Location"].unique())
df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].str.title() 
print(df["Location"].unique())
