#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:38:06 2018

@author: chriskwan
"""

import csv, numpy as np


# =============================================================================
# with open('NYPD_Complaint_Data_Current_YTD.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     total = 0
#     vect_lat = []
#     vect_long = []
#     for row in reader:
#         if row['Latitude'] == '':
#             vect_lat.append(row['Latitude'])
#         if row['Longitude'] == '':
#             vect_long.append(row['Longitude'])
#             
#     #print(vect_lat)
#     print('vect_long:' + str(len(vect_long)))
#     print('----------------------------')
#     print('vect_lat:' + str(len(vect_lat)))
# =============================================================================
    
with open('NYPD_Complaint_Data_Current_YTD.csv', 'rb') as inp, open('edit.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[23] != '' and row[24] != '':
            writer.writerow(row)
                
