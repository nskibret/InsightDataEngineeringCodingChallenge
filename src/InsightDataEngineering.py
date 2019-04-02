#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:44:16 2019

@author: nskibret
"""


class PurchaseAnalytics(object):
    
    def __init__(self,  order_products_file, products_input_file,  output_file_dir):
        
        self.order_products_input_file = order_products_file
        self.products_input_file = products_input_file
        self.output_file_dir = output_file_dir
        
        #a dictionary
        self._products = {}   # product_id as dictionary key and reorder values
        self._order_products = {}
        self.stat_per_department = {}
        
    
    def read_data(self):
        
         with open(self.order_products_input_file, 'r') as order_products_data:
             order_products_data.readline()
             
             for line in order_products_data:
                row = line.split(",")
            
                self._order_products[row[1]] = int(row[-1][:-1])
           
            
        
         with open(self.products_input_file, 'r') as products_data:
            products_data.readline()
            for line in products_data:
                row = line.split(",")
                self._products[row[0]] = row[3][:-1]       
            
       
            
            
    
        
        
    def write_data_to_disk(self):
        
        
        pass
        
    
    def find_order_statistics(self):
        
        for prod_id in self._products:
            department_id = self._products[prod_id]
            is_reorder = self._order_products[prod_id]
            
            if department_id in self.stat_per_department:
                self.stat_per_department[department_id][0] += 1
                if is_reorder==0:
                    self.stat_per_department[department_id][1] += 1
                
            else:
                
                self.stat_per_department[department_id] = [1,0,0]
                
                if is_reorder==0:
                    self.stat_per_department[department_id][1] += 1
                
            
        
        
        
        
        
        
    def calculate_percentage_values(self):
        
        
        for department_id in self.stat_per_department:
            self.stat_per_department[department_id][2] = \
            float(self.stat_per_department[department_id][1])/\
            self.stat_per_department[department_id][0]
    
    
    def print_data(self):
        print("Product ID   Reordered")
        for key in self._order_products:
            print(" {}:       {}".format(key, self._order_products[key]))
            
        print("Product ID   Department ID")
        for key in self._products:
            print(" {}:       {}".format(key, self._products[key]))
            
        print("Department ID      n_order       n_first_time_order")
        for key in self.stat_per_department:
            val = self.stat_per_department[key]
            
            print("{}     {}      {}    {}".format(key, val[0], val[1], val[2]))
        
        
        
        
        
    