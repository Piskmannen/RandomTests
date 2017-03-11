# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 12:59:23 2017

@author: Robert
"""

F=0
#if C < -273.15:
 #   print("That number is lower than the lowest possible temperature! Try again")
#else:
  #  conversion(C)
temperatures=[10,-20,-289,100]
def conversion(input):
    if input>-273.15:
        F=input*9/5+32
        return F
    else:
        return"That is too cold!"
for t in temperatures:
    print(conversion(t))




