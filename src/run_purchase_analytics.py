#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:22:41 2019

@author: nskibret
"""

import argparse


from InsightDataEngineering import PurchaseAnalytics



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", help="input directory")
    parser.add_argument("output_dir", help="output directory")
    parser.add_argument("products_fname", help="file name for products")
    parser.add_argument("order_products_fname", help="file name for order products")
    
    file_location = parser.parse_args()
    
    input_dir = file_location.input_dir
    output_dir = file_location.output_dir
    file1 = file_location.order_products_fname
    file2 = file_location.products_fname
    
    test = PurchaseAnalytics(input_dir, output_dir, file1, file2)
    test.read_purchase_data()
    test.find_order_statistics()
    test.calculate_percentage_values()
    test.write_data_to_disk()
    #test.print_data()
    print("Successfully completed")
