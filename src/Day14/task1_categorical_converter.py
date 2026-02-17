# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:23:42 2026

@author: ADEEKSHA
"""

import pandas as pd
cars = pd.read_csv("cars.csv")
cars["Transmission"] = cars["Transmission"].map({"Manual":0, "Automatic":1})
cars = pd.get_dummies(cars, columns=["Color"], drop_first=True)
print(cars)

# Explanation:
# Label encoding is used for binary data (Transmission).
# One-hot encoding is used for nominal data (Color) because colors have no order.
# If we assign numbers like Red=1, Blue=2, Green=3, the model may think Green > Red,
# which is incorrect. drop_first=True removes one dummy column to avoid multicollinearity
# (dummy variable trap).