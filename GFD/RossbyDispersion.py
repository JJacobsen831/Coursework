# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:10:32 2020

@author: Jasen
"""
import numpy as np
import matplotlib.pyplot as plt

#dispersion relation of rossby wave
Beta = 10**(-11)
Ri = np.sqrt(9.81*3800)/(2*7.29*10**(-5)*np.sin(45))

k = np.linspace(-10/Ri, 10/Ri, num = 50)

w = -Beta*k/(k**2+Ri**(-2))

#plt.figure
#plt.plot(k,w)
#plt.show()

(Ri -1)/Ri**2

#dispersion relation of an "equatorial" rossby wave
g = 9.81
H = 3800

#assume wavenumber is much smaller than 1/Ri
k = (1/Ri)/10000


y = np.linspace(0.000001,0.00001, num = 50)

R_eq = g*H/((Beta*y)**2)

c = -(R_eq)*Beta/(R_eq*k**2+1)

plt.figure
plt.plot(y, R_eq)
plt.show