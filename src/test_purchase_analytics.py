#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 01:58:35 2019

@author: nskibret
"""
import os
import unittest

from InsightDataEngineering import PurchaseAnalytics


input_dir = 'input/'
output_dir = 'output/'
product = 'products.csv'
order_product = 'order_products.csv'


class TestPurchaseAnalytics(unittest.TestCase):
    
    def test_read_purchase_data(self):
        # test if data is read properly
        purchase = PurchaseAnalytics(input_dir, output_dir, order_product, product)
        purchase.read_purchase_data()
        purchase.find_order_statistics()
        purchase.calculate_percentage_values()
        keys = list(purchase.stat_per_department.keys())
        values = list(purchase.stat_per_department.values())
        
        self.assertTrue(isinstance(purchase.stat_per_department, dict))
        self.assertTrue(isinstance(keys[0], int))
        self.assertTrue(isinstance(values[0], list))
        
        
        
    def test_data_written_to_disk(self):
        # test if output written to disk
        purchase = PurchaseAnalytics(input_dir, output_dir, product, order_product)
        purchase.read_purchase_data()
        purchase.find_order_statistics
        purchase.write_data_to_disk()
        path = os.listdir(output_dir)
        rep = ''
        for fname in path:
            if fname == 'report.csv':
                rep = fname
            
        self.assertTrue(rep == 'report.csv')
        

    
suite = unittest.TestLoader().loadTestsFromModule(TestPurchaseAnalytics())
unittest.TextTestRunner().run(suite)
    