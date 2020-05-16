# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:10:32 2020

@author: Jasen
"""
import numpy as np
import matplotlib.pyplot as plt


Beta = 10**(-11)
Ri = np.sqrt(9.81*3800)/(2*7.29*10**(-5)*np.sin(45))

k = np.linspace(-10/Ri, 10/Ri, num = 50)

w = -Beta*k/(k**2+Ri**(-2))

plt.figure
plt.plot(k,w)
plt.show()

(Ri -1)/Ri**2

