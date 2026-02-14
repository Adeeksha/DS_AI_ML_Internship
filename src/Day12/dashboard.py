# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 13:53:28 2026

@author: ADEEKSHA
"""

import matplotlib.pyplot as plt
categories=['Electronics','Clothing','Home']
sales=[300,450,200]
months=[1,2,3,4,5]
revenue=[100,200,300,400,500]
plt.subplot(1,2,1)
plt.bar(categories,sales)
plt.subplot(1,2,2)
plt.plot(months,revenue)
plt.tight_layout()
plt.show()