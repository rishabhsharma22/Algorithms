# -*- coding: utf-8 -*-
"""
Created on Fri May 25 01:08:59 2018

@author: Rishabh Sharma
"""

def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
