# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:12:45 2026

@author: ADEEKSHA
"""

import pandas as pd
grades=pd.Series([85, None, 92, 45, None, 78, 55])
missing=grades.isnull()
filled_grades=grades.fillna(0)
filtered_scores=filled_grades[filled_grades>60]
print("Original Series:")
print(grades)
print("\n Missing Values(True means missing):")
print(missing)
print("\nFilled Series (Missing replaced with 0):")
print(filled_grades)
print("\nScores Greater Than 60:")
print(filtered_scores)