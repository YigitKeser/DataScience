#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:59:56 2020

@author: yigitkeser
ID : 311904016
Paranthesis Checker
"""

from MyStack_module import MyStack
from data_module import Data

input_file = Data.read_data_into_str('input.txt')
openers = ["(", "{", "["]
closers = [")", "}", "]"]
paranthesis =  openers + closers
ms = MyStack()

def run():
    for item in range(0,len(input_file)):
        print('***Checking expression {}***'.format(item+1))
        counter = 0
        opener_counter = 0

        for char in input_file[item]:
            if char in openers:
                print('Opener dedected pushing : "{}"'.format(char))
                ms.push(char)
                ms.print_stack()
                opener_counter += 1
                
            if char in closers:
                if ms.top() in openers:
                    if closers.index(char) == openers.index(ms.top()):
                        print('Closer "{}" dedected popping "{}"'.format(char,ms.top()))
                        ms.pop()
                        opener_counter -= 1
                        ms.print_stack()
                    else:
                        print('When theres no "opener" in the stack "closer" : "{}" dedected'.format(char))
                        print('Expression is {} incorrect\n'.format(item+1))
                        break
                        
            if counter + 1 == len(input_file[item]):
                if ms.get_size() is not True and opener_counter == 0:
                    print('Expression {} is correct\n'.format(item+1))
                else:
                    print('Expression {} is incorrect\n'.format(item+1))
            counter += 1
            
def run_bonus():
    for item in range(0,len(input_file)):
        print('***Checking expression {}***'.format(item+1))
        counter = 0
        opener_counter = 0
        string = 0
        for char in input_file[item]:
            if char == "'":
                string+=1
                
            if char in openers and string%2 == 0:
                print('Opener dedected pushing : "{}"'.format(char))
                ms.push(char)
                ms.print_stack()
                opener_counter += 1
                
            if char in closers and string%2 == 0:
                if ms.top() in openers:
                    if closers.index(char) == openers.index(ms.top()):
                        print('Closer "{}" dedected popping "{}"'.format(char,ms.top()))
                        ms.pop()
                        opener_counter -= 1
                        ms.print_stack()
                else:
                    print('When theres no "opener" in the stack "closer" : "{}" dedected'.format(char))
                    print('Expression is {} incorrect\n'.format(item+1))
                    break
                        
            if counter + 1 == len(input_file[item]):
                if ms.get_size() is not True and opener_counter == 0:
                    print('Expression {} is correct\n'.format(item+1))
                else:
                    print('Expression {} is incorrect\n'.format(item+1))
            counter += 1
    

run()
#run_bonus()

        
        
        