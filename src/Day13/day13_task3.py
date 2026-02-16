# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:41:44 2026

@author: ADEEKSHA
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("housing.csv")
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
print("Correlation Table:\n", corr)
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df["Price"] < lower) | (df["Price"] > upper)]
print("\nOutlier Rows:\n", outliers)
sns.boxplot(y="Price", data=df)
plt.title("Outliers in Price")
plt.show()
