# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:43:58 2026

@author: ADEEKSHA
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data = pd.DataFrame({
    "Age":[22,25,30,35,40,45,50],
    "Salary":[25000,30000,50000,65000,80000,90000,120000]
})
std_scaler = StandardScaler()
std_scaled = std_scaler.fit_transform(data)
std_df = pd.DataFrame(std_scaled, columns=data.columns)
mm_scaler = MinMaxScaler()
norm_scaled = mm_scaler.fit_transform(data)
norm_df = pd.DataFrame(norm_scaled, columns=data.columns)
plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(data["Salary"], bins=5)
plt.title("Original Salary")
plt.subplot(1,3,2)
plt.hist(std_df["Salary"], bins=5)
plt.title("Standardized Salary")
plt.subplot(1,3,3)
plt.hist(norm_df["Salary"], bins=5)
plt.title("Normalized Salary")
plt.tight_layout()
plt.show()

# Explanation:
# Feature scaling is necessary because distance-based algorithms like KNN and SVM
# depend on magnitude. Salary values are much larger than Age, so the model would
# treat salary as more important. After scaling, all features contribute equally.
# StandardScaler is preferred for algorithms assuming normal distribution (KNN/SVM),
# while MinMaxScaler is useful when bounded values (0–1) are required.
