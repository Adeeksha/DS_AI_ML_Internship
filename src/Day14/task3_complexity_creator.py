# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:01:04 2026

@author: ADEEKSHA
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([1,4,9,16,25,36,49,64,81,100])
model_linear = LinearRegression()
model_linear.fit(X,y)
y_pred_linear = model_linear.predict(X)
r2_linear = r2_score(y, y_pred_linear)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model_poly = LinearRegression()
model_poly.fit(X_poly,y)
y_pred_poly = model_poly.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)
print("R2 Score (Linear):", r2_linear)
print("R2 Score (Polynomial):", r2_poly)

#R² increased from 0.95 to 1.0 after adding polynomial features.
#Therefore, curved features helped the model fit the nonlinear data.