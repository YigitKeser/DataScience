#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:36:03 2020

@author: yigitkeser
"""

import numpy as np
from matplotlib import pyplot as plt

f_x = lambda x: 0.005*(x**4) - 0.35*(x**2) - 0.4*x + 10
f_x_derivative = lambda x: 0.02*(x**3) - 0.7*x - 0.4

x = np.linspace(-8,10,1000)
plt.plot(x, f_x(x))
plt.show()

def plot_gradient(x, y, x_vis, y_vis):
    plt.subplot(1,1,1)
    plt.scatter(x_vis, y_vis, c = "b")
    plt.plot(x, f_x(x), c = "r")
    plt.title("Gradient Descent")
    plt.show()

def gradient_descent(x_start, precision, learning_rate):
    print('Start Point:', x_start)
    x_grad = [x_start]
    y_grad = [f_x(x_start)]
    while True:
        x_start_derivative = - f_x_derivative(x_start)
        x_start += (learning_rate * x_start_derivative)
        x_grad.append(x_start)
        y_grad.append(f_x(x_start))
        if abs(x_grad[len(x_grad)-1] - x_grad[len(x_grad)-2]) <= precision:
            break

    print("Learning Rate:" ,learning_rate)
    print("Local minimum occurs at: {:.4f}".format(x_start))
    print("y value at local minimum: {:.4f}".format(f_x(x_start)))
    print("Number of steps taken:",len(x_grad)-1 , '\n')
    plot_gradient(x,f_x,x_grad, y_grad)



gradient_descent(0.2,0.001,0.2)
gradient_descent(9.4,0.001,0.2)
gradient_descent(-1.1,0.001,0.2)
gradient_descent(-7.8,0.001,0.2)

gradient_descent(0.2,0.001,0.01)
gradient_descent(9.4,0.001,0.01)
gradient_descent(-1.1,0.001,0.01)
gradient_descent(-7.8,0.001,0.01)

#Using 10 as learning rate caused overflow error and i couldnt handle it.I used 1 instead.
gradient_descent(0.2,0.001,1)
gradient_descent(9.4,0.001,1)
gradient_descent(-1.1,0.001,1)
gradient_descent(-7.8,0.001,1)
