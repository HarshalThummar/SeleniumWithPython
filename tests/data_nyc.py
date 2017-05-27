#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:32:57 2017

@author: harshal
"""

import numpy as np
import pandas as pd

data = pd.read_csv("/home/harshal/Documents/pythonSelenium/env/data.csv")

sku_list = list(data.iloc[:,1])
master_sku = []
category =[]
category_diamond =[]
split_sku =[]
for i in sku_list:
    j = i.split('-')
    split_sku.append(j)
    master_sku.append(j[0])
    
data['SKU'] = master_sku

index_cp=[]
index_mpd=[]
index_pd=[]
index_pd2=[]
index_sp=[]
for i in range(len(data['SKU'])):
    if 'CP0' in data.ix[i,'SKU']:
        index_cp.append(i)
    if 'MPD0' in data.ix[i,'SKU']:
        index_mpd.append(i)
    if 'PD00' in data.ix[i,'SKU']:
        index_pd.append(i)
    if 'PD02' in data.ix[i,'SKU'] or 'PD03' in data.ix[i,'SKU']:
        index_pd2.append(i)
    if 'SP0' in data.ix[i,'SKU']:
        index_sp.append(i)
        
data_cp = data.iloc[index_cp,:]



      
category =[]
for j in split_sku:
    try:
        if j[1]=='WA':
            category.append('White')
        elif j[1] == 'YA':
            category.append('Yellow')
        else:
            category.append('')
    except:
        category.append('')
    
category_diamond=[]
for j in split_sku:
    try:
        if j[1] == 'DAM' or j[2] == 'DAM':
            category_diamond.append('Amethyst')
        elif j[1] == 'DAQ' or j[2] == 'DAQ':
            category_diamond.append('Aquamarine')
        elif j[1] == 'DBT' or j[2] == 'DBT':
            category_diamond.append('Blue Topaz')
        elif j[1] == 'DCT' or j[2] == 'DCT':
            category_diamond.append('Citrine')
        elif j[1] == 'DGA' or j[2] == 'DGA':
            category_diamond.append('Green Amethyst')
        elif j[1] == 'DGT' or j[2] == 'DGT':
            category_diamond.append('Garnet')
        elif j[1] == 'DLCE' or j[2] == 'DLCE':
            category_diamond.append('Lab Created Emerald')
        elif j[1] == 'DLCR' or j[2] == 'DLCR':
            category_diamond.append('Lab Created Ruby')
        elif j[1] == 'DLCS' or j[2] == 'DLCS':
            category_diamond.append('Lab Created Sapphire')
        elif j[1] == 'DPD' or j[2] == 'DPD':
            category_diamond.append('Peridot')
        elif j[1] == 'DPT' or j[2] == 'DPT':
            category_diamond.append('Pint Topaz')
        elif j[1] == 'DSQ' or j[2] == 'DSQ':
            category_diamond.append('Smokey Quartz')
        else:
            category_diamond.append('')
    except:
        category_diamond.append('')
    
    
    
len(category_diamond)
len(category)
data['SKU'] = master_sku
data['category'] = category
data['sub_category'] = category_diamond
