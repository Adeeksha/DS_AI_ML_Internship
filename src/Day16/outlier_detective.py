# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:36:43 2026

@author: ADEEKSHA
"""

import pandas as pd
import numpy as np

np.random.seed(42)


scores = np.random.normal(loc=70, scale=10, size=1000)
data = pd.DataFrame({'Score': scores})


mu = data['Score'].mean()
sigma = data['Score'].std()


data['z_score'] = (data['Score'] - mu) / sigma


outliers = data[np.abs(data['z_score']) > 3]

print("Mean (μ):", round(mu,2))
print("Standard Deviation (σ):", round(sigma,2))
print("\nStatistical Outliers (|Z| > 3):")
print(outliers)
