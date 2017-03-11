# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:45:10 2017

@author: Robert
"""

file=open("C:\\Users\\Robert\\Downloads\\example.txt",'w')
file.write("Line 7")
file.close()
#content=file.read()
#print(content)

file=open("C:\\Users\\Robert\\Downloads\\example.txt",'a')
file.write("blabla")
file.write("bdgfsfdsffa")
file.close()

