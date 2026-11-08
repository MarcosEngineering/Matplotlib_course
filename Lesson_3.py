# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:24:32 2026

@author: mcamp
"""

import matplotlib.pyplot as plt
import numpy as np

# Our first simple Object-Oriented example

fig,ax = plt.subplots()
x= np.linspace(0,10,100)
ax.plot(x,np.sin(x))
ax.set_title("Object-Oriented Style")
plt.show()

# Create a 2x1 grid, sharing the X axis
fig, (ax1,ax2) = plt.subplots(2,1, sharex=True)

ax1.plot(x,np.sin(x),'r')
ax1.set_ylabel('Sine')

ax2.plot(x,np.cos(-x),'g')
ax2.set_ylabel('Cosine')
plt.show()

fig,ax1=plt.subplots()
ax1.plot(x,x**2,'g-')
ax1.set_ylabel('Square Area',color='g')

ax2 = ax1.twinx() # Create a second Yaxuis sharing the same X-axis
ax2.plot(x,x**3, 'b--')
ax2.set_ylabel('Cube Volume', color='b')
plt.show()

# Create a explonential curve ad log scale

fig,ax=plt.subplots()
ax.plot(x, np.exp(x))
ax.set_yscale('log')
plt.show()

# example of  times-series data

import datetime
import matplotlib.dates as mdates

dates = [datetime.date(2023, 1, i) for i in range(1, 10)]
values = np.random.rand(9)

fig, ax = plt.subplots()
ax.plot(dates, values)

# Formatting the X-axis ticks

ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()
plt.show()

# Example of Typograpy, Latex and andvanced Visual

fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
# Using LaTeX for mathematical symbols
ax.set_title(r'Equation: $\alpha > \beta$ and $y = \sin(x)$', fontsize=16)
plt.show()

# Example rendering a colour 2D contour Map

X, Y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
Z = np.sin(X) * np.cos(Y)

fig, ax = plt.subplots()
contour = ax.contourf(X, Y, Z, cmap='viridis')
fig.colorbar(contour) # Adds a legend for the colors






