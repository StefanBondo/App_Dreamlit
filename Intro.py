#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:50:11 2026

@author: stefanbondo
"""

import pandas as pd

housedata = pd.read_csv("dataVideoMLIII.csv")

hel="stefan"
tal=5
tal2=5.4
tal3=66

mylist=list()

mylist.append("Viggo")
mylist.append("Kurt")
mylist.append("Lone")

for elem in mylist:
    print(elem)
    
[print(elem) for elem in mylist if elem.startswith("L")]

def myFun (x,y):
    retval = x+y
    return(retval)

myFun(5, 6)