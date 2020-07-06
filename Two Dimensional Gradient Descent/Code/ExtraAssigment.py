#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:01:54 2020

@author: yigitkeser
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def iterate_algorithm(x,y,learning_rate,precision):
    #Creating Lists for data points and function results
    x_list = [x]
    y_list = [y]
    w_list = [fxy(x,y)]
    #Gradient descent loop
    while True:
        dx = d_fx(x,y) 
        dy = d_fy(x,y) 
        change_x = learning_rate * -dx
        change_y = learning_rate * -dy
        x += change_x
        y += change_y
        x_list.append(x) 
        y_list.append(y)
        w_list.append(fxy(x,y))
        learning_rate *= 0.99 #Decreasing learning rate
        if abs(w_list[len(w_list)-1] - w_list[len(w_list)-2]) <= precision:
            break

        
    print("Learning Rate:" ,learning_rate)
    print("Local minimum occurs at: {:.4f}".format(w_list[-1]))
    print("x value at local minimum: {:.4f}".format(x_list[-1]))
    print("y value at local minimum: {:.4f}".format(y_list[-1]))
    print("Number of steps taken:",len(w_list)-1)
    
    return np.array(x_list),np.array(y_list),np.array(w_list)

#Function and derivatives
fxy = lambda x,y: -0.3*(x**4) - 0.3*(y**4) + 5*(x**2) + 5*(y**2) -x -5*y +10 # Function
d_fx = lambda x,y: -1.2*(x**3) + 10*x -1 #derivative by x
d_fy = lambda x,y: -1.2*(y**3) + 10*y -5 #derivative by y

#Collecting results from algorithm
results_x , results_y , results_w = iterate_algorithm(x=-2.9,y=-2,learning_rate=0.02,precision=0.001)

#Meshgrid
x_ , y_ = np.meshgrid(np.linspace(-3.5,3.5,1000),np.linspace(-4,3,1000))

#Calculating results for meshgrid points
fresults = fxy(x_,y_)

#Contour plot 2D
plt.contour(x_,y_,fresults, levels = np.arange(1,100,3))
plt.scatter(results_x, results_y, c = "b")
plt.show()
plt.close()

#Contour plot 3D
fig = plt.figure(figsize =(14, 9)) 
ax = Axes3D(fig)

ax.plot_surface(x_, y_, fresults) 
ax.scatter(results_x, results_y, results_w , marker = "*" , color ="r" , s=999)
ax.dist = 9
#ax.view_init(azim=0 , elev=270)
plt.show()

