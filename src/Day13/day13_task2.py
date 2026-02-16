# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:41:44 2026

@author: ADEEKSHA
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("housing.csv")
sns.scatterplot(x="Area", y="Price", data=df)
plt.title("Area vs Price")
plt.xlabel("Square Footage (Area)")
plt.ylabel("Price")
plt.show()

sns.boxplot(x="City", y="Price", data=df)
plt.title("City vs Price Distribution")
plt.xticks(rotation=45)
plt.show()
