# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:48:04 2020

@author: Jasen
"""
#stability of mean jet stream path

#Import packages
import os
os.chdir("/Users/Jasen/Documents/GitHub/NumericalMethods")
import numpy as np
import matplotlib.pyplot as plt
from NumericalMethodFuns import EulerMethod as EM

# Model parameters
U = 40 # m/s                        <- scale velocity of jet stream
L = 570*1000 # m                    <- width of jet stream
Beta = 1.61*10**(-11) # m^-1 s^-1   <- constant beta

#Define mean, 1st and 2nd derivs
U_bar = lambda y : U*np.exp(-y**2/(2*L**2))
dU_dy = lambda y : -y*U/(L*2)*np.exp(-y**2/(2*L))
d2U_dy2 = lambda y : (((U/(L**4))*(y**2)) - U/(L**2))*np.exp(-(y**2)/(2*L**2))

#Use Euler method to find where 2nd deriv crosses beta
y_run = 0
tau = 10
while d2U_dy2(y_run) <= Beta:
    U_new = EM(U_bar(y_run),dU_dy(y_run),tau)
    
    y_run = y_run+tau

# save output for display
thresh = str(y_run)
lab = thresh+' m'

#initialize plot
y = np.linspace(-2*L, 2*L, num = 100)
plt.figure()

#plot second derivatives and lines
plt.plot(d2U_dy2(y), y)
plt.plot(np.ones((len(y),))*1.61*10**(-11), y)
plt.plot(np.linspace(np.min(d2U_dy2(y)), np.max(d2U_dy2(y)), 50), np.ones(50, )*y_run)

#add labels and legend
plt.text(-1.25*10**(-10), y_run+100, lab)
plt.legend(('2nd Deriv.', 'Beta', 'Instability Threshold'), loc='lower left')
plt.ylabel('y [m]')
plt.xlabel('Second Derivative of U_bar')

#save and show plot
#plt.savefig('/Users/Jasen/Documents/Coursework/GeophysicalFluidDynamics/ProblemSet5/MeanJetStreamStability.png')
plt.show()