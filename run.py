#Sample calculator

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:32:16 2020

@author: tobiasisabella
"""

print("**********************Calculator Python*********************")

print("Select the desired operation number:")

print('1 - Sum')
print('2 - Subtraction')
print('3 - Multiplication')
print('4 - Division')

#The use of float is so that the code receives the value as a number and not as a string
selection = float(input("Enter your option (1/2/3/4):"))

if selection < 1 or selection > 4:
    print("Invalid number")
    print("Please enter a valid option")
    
else:

    first = float(input("Enter the first number:"))

    second = float(input("Enter the second number:"))


    if selection == 1: 
        print(first, "+", second, "=", first + second)
    
    elif selection == 2: 
        print(first, "+", second, "=", first - second)
        
    elif selection == 3: 
        print(first, "+", second, "=", first * second)
        
    if selection == 4: 
        print(first, "+", second, "=", first / second)
