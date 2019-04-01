#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:44:16 2019

@author: nskibret
"""

import csv

class PurchaseAnalytics(object):
    
    def __init__(self, input_file_dir, output_file_dir):
        
        self.input_dir = input_file_dir
        self.output_dir = output_file_dir
        
        #a dictionary
        self._products = {}
        self._order_products = {}
        self.department_id = []
        self.stat_per_department = {}
        
    
    def read_data(self):
        
        
        with open(self.input_dir) as data:
            purchase_data  = csv.reader(data, delimiter=',')
           
            for row in purchase_data:
                self._products[row[1]] = row[3]
            del self._products['product_id']
            
            
    
        
        
    def write_data_to_disk(self):
        
        
        pass
        
    
    def find_order_statistics(self):
        
        pass
        
        
        
        
        
        
    def calculate_percentage_values(self):
        
        
        pass
    
    def print_data(self):
        print("Product ID          Reordered")
        for key in self._products:
            print(" {}:  {}".format(key, self._products[key]))
        
        
        
        
        

        
file = 'order_products.csv'

test = PurchaseAnalytics(file, './')
test.read_data()
test.print_data()
        
        
        
        
    
    
    
    
    