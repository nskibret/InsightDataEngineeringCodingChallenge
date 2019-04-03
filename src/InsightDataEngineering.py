#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:44:16 2019

@author: nskibret
"""
import os

class PurchaseAnalytics(object):
    """This class retrieves and performes analysis on purchase data.
    
    
    Attributes:
        self.input_dir (str): directory containing input data
        self.output_dir (str): directory for writing the output data to
        self.order_products_input_file (str): path containing order products input data
        self.products_input_file (str): path containing products input data
        self.stat_per_department (dict): a dictionary of lists
        
        
        """
    
    def __init__(self,  input_dir, output_dir, order_fname, products_fname):
        """initialize variables
        
        Args:
            input_path (str): The path containing input data.
            output_path (str): The path for writing the output data.
            products_fname (str): file name containing products 
            order_fname (str): file name of order products
            
        
        """
        
        # directory holding input data
        self.input_dir = input_dir 
        
        # directory to write output data to
        self.output_dir = output_dir 
        
        # path containing order products file (e.g. order_products.csv)
        self.order_products_input_file = os.path.join(self.input_dir, \
                                                      order_fname)
        # path containing products file (e.g. products.csv)
        self.products_input_file = os.path.join(self.input_dir, \
                                                products_fname)
        
        # define a dictionary to hold reading from product.csv file
        # product_id as the key and reorder field as value
        self._products = {}   
        
        # define a dictionary to hold reading from order_products.csv file
        # product_id as the key and department_id as value
        self._order_products = {}
        
        # define a dictionary of lists
        # this will hold department_id as its key and 
        # a list [number_of_orders, number_of_first_orders, percentage] as values
        self.stat_per_department = {}
        
    
    def read_purchase_data(self):
        """read purchase data from disk.
        
        """
        # 
        with open(self.order_products_input_file, 'r') as order_products_data:
             order_products_data.readline() # skip header
             
             for line in order_products_data:
                row = line.split(",") # comma separated values
                
                # we are interested only on second and last column 
                # (i.e. product_id and reordered fields)
                # convert reordered field to int
                try: # catch if integer conversion fails
                    self._order_products[row[1]] = int(row[-1][:-1]) 
                
                except ValueError:
                    continue # continue reading next line
                
           
            
        # 
        with open(self.products_input_file, 'r') as products_data:
            products_data.readline() # skip header
            
            for line in products_data:
                row = line.split(",") # comma separated values
                
                # we are interested only on the first and last column \
                # (i.e. product_id and department_id fields)
                # convert department_id field to integer, for sorting purpose
                try: # catch if integer conversion fails
                    self._products[row[0]] = int(row[3][:-1])  
                    
                except ValueError:
                    continue # continue reading next line
            
       
        
        
    def write_data_to_disk(self):
        """write order statistics to disk.
        
        """
        
        # create path to store output data 
        output_path = os.path.join(self.output_dir, 'report.csv')
        
        # sort department_id, to store results in a sorted order
        sorted_department_id = sorted(self.stat_per_department.keys())
        
        with open(output_path, 'w') as report:
            
            #write header
            report.write("department_id,number_of_orders,\
                         number_of_first_orders,percentage\n")
            
            for dep_id in sorted_department_id:
                # get the list - [number_of_orders, number_of_first_orders, percentage]
                stats = self.stat_per_department[dep_id]
                
                # write to file in the order (department_id, number of orders, 
                # number of first orders, percentage)
                report.write("{},{},{},{:.2f}\n".format(dep_id, stats[0], stats[1], stats[2]))
        
    
    def find_order_statistics(self):
        """find number of orders and number of first orders.
        
        """
        
        # variable to check if reorder is 0 or 1
        is_reorder = None
        
        for prod_id in self._products:
            department_id = self._products[prod_id]
            
            # check if product_id in products also exists in order_products
            if prod_id in self._order_products:
                is_reorder = self._order_products[prod_id] # get reorder (1 or 0)
            else:
                # there is no corresponding product_id number in order_products
                continue # skip this product_id
                
            
            if department_id in self.stat_per_department:
                
                # check if reorder is valid (either 0 or 1)
                if is_reorder == 0 or is_reorder ==1:
                    # update number of orders
                    self.stat_per_department[department_id][0] += 1
                    
                    # if reorder is 0, update number_of_first_orders
                    if is_reorder==0:
                        self.stat_per_department[department_id][1] += 1
                
            else:
                
                # check if reorder is valid (either 0 or 1)
                if is_reorder == 0 or is_reorder == 1:
                    # first time encountered department id
                    # initialize it to a list, 
                    # first element set to 1, valid reorder
                    self.stat_per_department[department_id] = [1,0,0]
                    
                    if is_reorder==0:
                        self.stat_per_department[department_id][1] += 1
                
            
        
    def calculate_percentage_values(self):
        """calculate percentage.
        
        find the ratio of number_of_first_orders to number_of_orders.
        result stored as third element in the dictionary of lists 
        self.stat_per_department.
        
        
        """
        
        for department_id in self.stat_per_department:
            self.stat_per_department[department_id][2] = \
            float(self.stat_per_department[department_id][1])/\
            self.stat_per_department[department_id][0]
    
    
    def print_data(self):
        """
        
        
        """
        
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
        
        
        
        
        
    