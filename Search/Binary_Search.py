# -*- coding: utf-8 -*-
"""
Created on Fri May 25 01:15:25 2018

@author: Rishabh Sharma
"""

def binary_search(arr,left,right,x):
    if right>=1:
        mid = left+(right-1) / 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,left,mid-1,x)
        else:
            return binary_search(arr,mid+1,right,x)
    else:
        return -1