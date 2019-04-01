#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:44:16 2019

@author: nskibret
"""
import heapq as hq

def k_most_frequent_elements(list_of_ints):
    
    """Return the k most frequent elements.
    
    Input:
        list_of_ints: a non empty list of integers
        
    Output:
             a list consisting of k most frequent elements in list_of_ints"""
    
    frequency_counts = {}
    
    for x in list_of_ints:
        frequency_counts[x] = frequency_counts.get(x, 0) + 1
      
    k_frequent_elemts = []
    
    
    