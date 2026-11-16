# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:02:57 2026

@author: mcamp


"""

# Example 3D Scatter Plot

from matplotlib import pyplot as plt
import numpy as np

# Set a consistent figure size

plt.rcParams['figure.figsize']= (8,6)

# Generate some random 3D data

np.random.seed(31)

mu=3
n=50

x=np.random.normal(mu,1,size=n)
y=np.random.normal(mu,1,size=n)
z=np.random.normal(mu,1,size=n)

# Initialize 3D axis
ax= plt.axes(projection='3d')
type(ax)

# Basic 3D scatter plot
ax.scatter3D(x,y,z, s=100, color= 'red')

ax.set_xlabel('X_axis')
ax.set_ylabel('Y_axis')
ax.set_zlabel('Z_axis')

# Rotate the camera: 45 degrees elavation, 215 degrees azimuth
ax.view_init(15,215)
plt.show()


# example 3D line PLots (helix)

from matplotlib import pyplot as plt
import numpy as np

omega = 3
z_line = np.linspace(0, 10, 100)
x_line = np.cos(omega * z_line)
y_line = np.sin(omega * z_line)

ax = plt.axes(projection='3d')
ax.plot3D(x_line, y_line, z_line, lw=2, color='red')
plt.show()



# example 3D Surface PLot

from matplotlib import pyplot as plt
import numpy as np

def function_z(x,y):
    return 50-(x**2+y**2)

N=10
x_values=np.linspace(-5,5,N)
y_values=np.linspace(-5,5,N)

# Create coordinate matrices
X,Y = np.meshgrid(x_values,y_values)

X.shape

Z=function_z(X,Y)
Z.shape

ax=plt.axes(projection='3d')
# add the grid for a wireframe
ax.plot_wireframe(X,Y,Z, color='black',lw=2)

#use cmap to add color gradient based on depth
ax.plot_surface(X,Y,Z,cmap='cividis', edgecolor='none')
plt.show()

# example line_magic 3D graph

import numpy as np
import matplotlib.pyplot as plt

# Python-safe way to run magic commands in a script
try:
    get_ipython().run_line_magic('matplotlib', 'qt')
except NameError:
    pass # Ignores the command if not running in an IPython environment

# Generate data
np.random.seed(35)
mu = 3
n = 50
x = np.random.normal(mu, 1, size=n)
y = np.random.normal(mu, 1, size=n)
z = np.random.normal(mu, 1, size=n)

# Create the figure and plot
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(x, y, z, s=100, edgecolor='black')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()





















