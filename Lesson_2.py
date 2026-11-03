# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 06:13:46 2026

@author: mcamp
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,1)
y=x**2

# 'ro--' means Red color, circle marker, dashed line
plt.plot(x,y,'ro--')
plt.show()

y2= x**2.5
# Multipline plotting with different style
plt.plot(x,y, 'b^-', label='Data 1')  # Blue, Triangle marker, solid line
plt.plot(x,y2, 'gs:', label='Data 2')  # Green, Square marker, dotted line
plt.show()

plt.plot(x,y,color='purple', linestyle='-.', linewidth=4, marker='D', markersize=8, markerfacecolor='yellow')
plt.xticks(np.arange(0,11,1)) # shows 0,1,2 ... 10
plt.show()

# Exemple of Histograme

data=np.random.randn(1000)
plt.hist(data, bins=10, color='skyblue',edgecolor='black')
plt.show()

# Exemple of Chart and Pie Chart

categories = ['A','B','C']
values = [10,25,15]
plt.bar(categories,values, color=['red','green','blue'])
plt.show()

explode = (0.1,0,0) # Pulls out the first slice
plt.pie(values, labels=categories, explode=explode, autopct='%1.1f%%')
plt.show()

# Exemple of Scatter Plots

x_scatter = np.random.rand(50)
y_scatter= np.random.rand(50)
colors=np.random.rand(50)
sizes=1000*np.random.rand(50)
plt.scatter(x_scatter,y_scatter,c=colors,s=sizes, alpha=0.5,cmap='viridis')
plt.show()

# Exemple of Polar Charts

ax= plt.subplot(111,projection='polar')
theta= np.linspace(0,2*np.pi,100)
r= np.abs(np.sin(2*theta))
ax.plot(theta,r)
plt.show()

# Exemple of Annotation, and Arrow
plt.plot(x,y)
plt.annotate('Local Maximum', xy=(4,16),xytext=(2,25),arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()


