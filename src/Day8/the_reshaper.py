# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:15:04 2026

@author: ADEEKSHA
"""

import numpy as np
data=np.arange(24)
reshaped_data=data.reshape(4,3,2)
transposed_data=reshaped_data.transpose(0,2,1)
print("Final Shape:", transposed_data.shape)
print("\nFinal Array:\n", transposed_data)
