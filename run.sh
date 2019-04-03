#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. 
#
#python ./src/purchase_analytics.py ./input/order_products.csv ./input/products.csv ./output/report.csv
python3 ./src/run_purchase_analytics.py ./input/ ./output products.csv order_products.csv
