# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:23:00 2026

@author: ADEEKSHA
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")

sns.histplot(df["Price"], kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)

sns.countplot(x="City", data=df)
plt.title("City Frequency")
plt.xticks(rotation=45)
plt.show()
