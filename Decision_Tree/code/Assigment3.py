#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:09:17 2020

@author: yigitkeser
"""

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import os


def calculate_ENT(data):
    target_variable = data[2]
    n_labels = len(target_variable)
    values , counts = np.unique(target_variable, return_counts=True)
    probs = counts / n_labels
    entropy = 0.0
    for i in probs:
        if i != 0:
            entropy -= i * math.log(i, 2)
        else:
            entropy += 0
    return entropy


def calculate_IG(data):
    IGx = []
    IGy = []
    for x in data[0]:
        left = data.loc[data[0] < x]
        right = data.loc[data[0] >= x]
        IGx.append((x,calculate_ENT(data) - len(left) / len(data) * calculate_ENT(left) - len(right) / len(data) * calculate_ENT(right)))
    for y in data[1]:
        down = data.loc[data[1] < y]
        up = data.loc[data[1] >= y]
        IGy.append((y,calculate_ENT(data) - len(down) / len(data) * calculate_ENT(down) - len(up) / len(data) * calculate_ENT(up)))
    return np.array(IGx),np.array(IGy)

def find_max_IG(data):
    x_values_gains,y_values_gains = np.array(calculate_IG(data))
    x_max_index = np.argmax(x_values_gains[:,1])
    y_max_index = np.argmax(y_values_gains[:,1])
    if x_values_gains[x_max_index][1] >= y_values_gains[y_max_index][1]:
        axis = 'x'
        return axis,x_max_index , x_values_gains[x_max_index][0] , x_values_gains[x_max_index][1]
    else:
        axis = 'y'
        return axis,y_max_index , y_values_gains[y_max_index][0] , y_values_gains[y_max_index][1]

def plot_boundry():
    if axis == 'y':
        plt.plot(data.loc[data[2] == 1][[0]],data.loc[data[2] == 1][[1]] , 'bo')
        plt.plot(data.loc[data[2] == 2][[0]],data.loc[data[2] == 2][[1]] , 'go')
        plt.plot([0,data.max()[0]] , [value,value] , label = str(axis)+'='+str(value)+' IG:'+str(info_gain))
        plt.legend()
    else:
        plt.plot(data.loc[data[2] == 1][[0]],data.loc[data[2] == 1][[1]] , 'bo')
        plt.plot(data.loc[data[2] == 2][[0]],data.loc[data[2] == 2][[1]] , 'go')
        plt.plot([value,value] ,[0,data.max()[0]] , label = str(axis)+'='+str(value)+' IG:'+str(info_gain))
        plt.legend()

def plot_IG(color,data):
    if axis == 'y':
        plt.plot(calculate_IG(data)[1][:,0] , calculate_IG(data)[1][:,1] , color)
    else:
        plt.plot(calculate_IG(data)[0][:,0] , calculate_IG(data)[0][:,1] , color)
        
def sub_data():
    if axis == 'y':
        down = data.loc[data[1] < value]
        up = data.loc[data[1] >= value]
        if calculate_ENT(up) >= calculate_ENT(down):
            sub_data = up
        else:
            sub_data = down
    else:
        left = data.loc[data[0] < value]
        right = data.loc[data[0] >= value]
        if calculate_ENT(left) >= calculate_ENT(right):
            sub_data = left
        else:
            sub_data = right
    return sub_data
    
    
data = pd.read_csv(os.path.join(os.path.dirname(__file__), "data/data.csv") , header = None)
max_depth = 3
depth = 1

while depth <= max_depth:
    depth += 1
    axis , index , value , info_gain = find_max_IG(data)
    plot_boundry()
    data = sub_data()

depth = 1
plt.figure()


data = pd.read_csv(os.path.join(os.path.dirname(__file__), "data/data.csv") , header = None)

while depth -1 <=max_depth - 1:
    axis , index , value , info_gain = find_max_IG(data)
    color = ['bo','go','ro','yo','co','mo']
    plot_IG(color[depth],data)
    depth +=1
    data = sub_data()




