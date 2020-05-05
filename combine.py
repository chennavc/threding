#!/usr/bin/env python
# coding: utf-8

# In[7]:




import os
import csv
import json
f2 = open('allproducts.csv', 'w')
f2.write("prod_id,prod_sku,prod_cat,prod_name\n")
f2.close()
f2 = open('allproducts.csv', 'a')
writer = csv.writer(f2, delimiter=',', lineterminator='\n')

for root, dirs, files in os.walk('output'):
    path = root.split(os.sep)
    
    for fn in files:
        fp = root + os.sep + fn
        print("Reading from the File: " + fp)
        
        with open(fp, 'r') as openfile:
            json_dictionary = json.load(openfile)
            prod_id = json_dictionary['prod_id']
            prod_sku = json_dictionary['prod_sku']
            prod_cat = json_dictionary['prod_cat']
            prod_name = json_dictionary['prod_name']
            row = [prod_id, prod_sku, prod_cat, prod_name]
            writer.writerow(row)
            print("Success writing :" + fp + " to allproducts.csv")
f2.close()


# In[ ]:




