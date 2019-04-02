#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:22:41 2019

@author: nskibret
"""
from InsightDataEngineering import PurchaseAnalytics



file1 = 'order_products.csv'
file2 = 'products.csv'

test = PurchaseAnalytics(file1, file2, './')
test.read_data()
test.find_order_statistics()
test.calculate_percentage_values()
test.print_data()