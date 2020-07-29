#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:41:05 2020

@author: yigitkeser
"""

class Data:
    '''csv reader'''
    def read_data_into_str(filename):
        with open(filename , 'r') as file:
            return file.readlines()