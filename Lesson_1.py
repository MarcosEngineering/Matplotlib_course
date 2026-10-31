# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:14:02 2026

@author: mcamp
"""

import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4]
y= [10,20,25,30]
plt.plot(x,y)
plt.show()

y2= [15,25,30,40]
plt.plot(x,y)
plt.plot(x,y2)
plt.show()

# Generate an array from 0 to 10 with 100 steps
t=np.linspace(0,10,100)
plt.plot(t,np.sin(t), label="Sine wave")
plt.plot(t,np.cos(t),label="Cosine Wave")
plt.title ('Basic Trigonometric Functions')
plt.legend(loc='upper left')
plt.axis([0,10,-1.5,1.5])
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.show()