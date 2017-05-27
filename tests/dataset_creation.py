#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 00:03:21 2017

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
for i in split_sku[:len(data_cp['SKU'])]:
    try:
        if i[1]=='WA':
            category.append('White')
        elif i[1] == 'YA':
            category.append('Yellow')
        else:
            category.append('')
    except:
        category.append('')

data_cp['category'] = category

main_title = []
for i in data_cp['Title']:
    if 'White' in i:
        main_title.append(i.replace('White',''))
    elif 'Yellow' in i:
        main_title.append(i.replace('Yellow',''))
        
        


new_descrip = []
for i in data_cp.iloc[:,3]:
    if 'white' in i:
        new_descrip.append(i.replace('white',''))
    elif 'yellow' in i:
        new_descrip.append(i.replace('yellow',''))
        
        

data_cp['main_title'] = main_title
data_cp['description'] = new_descrip
new_df = data_cp.drop_duplicates(subset =  ['main_title'],keep="first")
new_df = new_df.reset_index()
###################################### VARIANTS
var_df = new_df.copy(True)

white_list = list(var_df.iloc[:,2])
yellow_list =[]
for i in white_list:
    yellow_list.append(i.replace('WA','YA'))

white_title_list = list(var_df.iloc[:,3])
yellow_title_list = []
for i in white_title_list:
    yellow_title_list.append(i.replace('White','Yellow'))



variant_df = var_df.iloc[:,[1,5,9,11,12]]

variant_df['white_sku'] = white_list
variant_df['yellow_sku'] = yellow_list
variant_df['white_title'] = white_title_list
variant_df['yellow]_title'] = yellow_title_list




##################################### MPD
data_mpd = data.iloc[index_mpd,:].reset_index()

split_sku_mpd = split_sku[index_mpd[0]:index_mpd[-1]+1]

category =[]
for i in split_sku_mpd:
    try:
        if i[1]=='WA' or i[2]=='WA':
            category.append('White')
        elif i[1] == 'YA' or i[2] =='YA':
            category.append('Yellow')
        else:
            category.append('')
    except:
        category.append('')


data_mpd['category'] = category

category_diamond=[]
for j in split_sku_mpd:
    try:
        if j[2] == 'DAM':
            category_diamond.append('Amethyst')
        elif j[2] == 'DAQ':
            category_diamond.append('Aquamarine')
        elif j[2] == 'DBT':
            category_diamond.append('Blue Topaz')
        elif j[2] == 'DCT':
            category_diamond.append('Citrine')
        elif j[2] == 'DGA':
            category_diamond.append('Green Amethyst')
        elif j[2] == 'DGT':
            category_diamond.append('Garnet')
        elif j[2] == 'LCE':
            category_diamond.append('Lab Created Emerald')
        elif j[2] == 'LCR':
            category_diamond.append('Lab Created Ruby')
        elif j[2] == 'LCS':
            category_diamond.append('Lab Created Sapphire')
        elif j[2] == 'DPD':
            category_diamond.append('Peridot')
        elif j[2] == 'DPT':
            category_diamond.append('Pint Topaz')
        elif j[2] == 'DSQ':
            category_diamond.append('Smokey Quartz')
        else:
            category_diamond.append('')
    except:
        category_diamond.append('')

################################################## PD

data_pd = data.iloc[index_pd,:].reset_index()

split_sku_pd = split_sku[index_pd[0]:index_pd[-1]+1]

category =[]
for i in split_sku_pd:
    try:
        if i[1]=='WA':
            category.append('White')
        elif i[1] == 'YA':
            category.append('Yellow')
        else:
            category.append('')
    except:
        category.append('')


data_pd['category'] = category

no_of_categories = data_pd.groupby('SKU').size()/3

category_diamond=[]
for j in split_sku_pd:
    try:
        if j[-1] == 'DAM':
            category_diamond.append('Amethyst')
        elif j[-1] == 'DAQ':
            category_diamond.append('Aquamarine')
        elif j[-1] == 'DBT':
            category_diamond.append('Blue Topaz')
        elif j[-1] == 'DCT':
            category_diamond.append('Citrine')
        elif j[-1] == 'DGA':
            category_diamond.append('Green Amethyst')
        elif j[-1] == 'DGT':
            category_diamond.append('Garnet')
        elif j[-1] == 'DLCE' or j[-1] == 'LCE':
            category_diamond.append('Lab Created Emerald')
        elif j[-1] == 'DLCR' or j[-1] == 'LCR':
            category_diamond.append('Lab Created Ruby')
        elif j[-1] == 'DLCS' or j[-1] == 'LCS':
            category_diamond.append('Lab Created Sapphire')
        elif j[-1] == 'DPD':
            category_diamond.append('Peridot')
        elif j[-1] == 'DPT':
            category_diamond.append('Pink Topaz')
        elif j[-1] == 'DSQ':
            category_diamond.append('Smokey Quartz')
        elif j[-1] == 'DEM' or j[-1] == 'EM':
            category_diamond.append('Emerald')
        elif j[-1] == 'RB' or j[-1]=='DRB':
            category_diamond.append('Ruby')
        elif j[-1] == 'SP' or j[-1] == 'DSP':
            category_diamond.append('Sapphire')
        else:
            category_diamond.append('')
    except:
        category_diamond.append('')
        
data_pd['sub_category'] = category_diamond

strip_category =[]
for i in split_sku_pd:
    try:
        if i[1]=='WA' or i[1] == 'YA':
            strip_category.append(i[0]+'-'+i[-1])
        else:
            strip_category.append(i[0]+'-'+i[-1])
    except:
        strip_category.append('')
        
        
data_pd['strip_category'] = strip_category

new_df_pd = data_pd.drop_duplicates(subset =  ['strip_category'],keep="first")

title = list(new_df_pd['Title'])
main_title =[]
for i in title:
    if 'Shaped Amethyst' in i:
        main_title.append(i.replace(' Amethyst ',' Gemstone '))
    elif 'Aquamarine' in i:
        main_title.append(i.replace(' Aquamarine ',' Gemstone '))
    elif 'Blue Topaz' in i:
        main_title.append(i.replace(' Blue Topaz ',' Gemstone '))
    elif 'Citrine' in i:
        main_title.append(i.replace(' Citrine ',' Gemstone '))
    elif 'Green Amethyst' in i:
        main_title.append(i.replace(' Green Amethyst ',' Gemstone '))
    elif 'Garnet' in i:
        main_title.append(i.replace(' Garnet ',' Gemstone '))
    elif 'Lab Created Emerald' in i:
        main_title.append(i.replace(' Lab Created Emerald ',' Gemstone '))
    elif 'Lab Created Ruby' in i:
        main_title.append(i.replace(' Lab Created Ruby ',' Gemstone '))
    elif 'Lab Created Sapphire' in i:
        main_title.append(i.replace(' Lab Created Sapphire ',' Gemstone '))
    elif 'Peridot' in i:
        main_title.append(i.replace(' Peridot ',' Gemstone '))
    elif 'Pink Topaz' in i:
        main_title.append(i.replace(' Pink Topaz ',' Gemstone '))
    elif 'Smokey Quartz' in i:
        main_title.append(i.replace(' Smokey Quartz ',' Gemstone '))
    elif 'Shaped Emerald' in i:
        main_title.append(i.replace(' Emerald ',' Gemstone '))
    elif 'Shaped Ruby' in i:
        main_title.append(i.replace(' Ruby ',' Gemstone '))
    elif 'Shaped Sapphire' in i:
        main_title.append(i.replace(' Sapphire ',' Gemstone '))
    else:
        main_title.append('')
        

new_df_pd['main_title'] = main_title


description  = list(new_df_pd['Product Description'])
main_descrip = []
for i in description:
    if 'shaped Amethyst' in i:
        main_descrip.append(i.replace(' Amethyst ',' Gemstone '))
    elif 'Aquamarine' in i:
        main_descrip.append(i.replace(' Aquamarine ',' Gemstone '))
    elif 'Blue Topaz' in i:
        main_descrip.append(i.replace(' Blue Topaz ',' Gemstone '))
    elif 'Citrine' in i:
        main_descrip.append(i.replace(' Citrine ',' Gemstone '))
    elif 'Green Amethyst' in i:
        main_descrip.append(i.replace(' Green Amethyst ',' Gemstone '))
    elif 'Garnet' in i:
        main_descrip.append(i.replace(' Garnet ',' Gemstone '))
    elif 'Lab Created Emerald' in i:
        main_descrip.append(i.replace(' Lab Created Emerald ',' Gemstone '))
    elif 'Lab Created Ruby' in i:
        main_descrip.append(i.replace(' Lab Created Ruby ',' Gemstone '))
    elif 'Lab Created Sapphire' in i:
        main_descrip.append(i.replace(' Lab Created Sapphire ',' Gemstone '))
    elif 'Peridot' in i:
        main_descrip.append(i.replace(' Peridot ',' Gemstone '))
    elif 'Pink Topaz' in i:
        main_descrip.append(i.replace(' Pink Topaz ',' Gemstone '))
    elif 'Smokey Quartz' in i:
        main_descrip.append(i.replace(' Smokey Quartz ',' Gemstone '))
    elif 'shaped Emerald' in i:
        main_descrip.append(i.replace(' Emerald ',' Gemstone '))
    elif 'shaped Ruby' in i:
        main_descrip.append(i.replace(' Ruby ',' Gemstone '))
    elif 'shaped Sapphire' in i:
        main_descrip.append(i.replace(' Sapphire ',' Gemstone '))
    else:
        main_descrip.append('')
        

new_df_pd['description'] = main_descrip

white_sku = []
yellow_sku = []
sku = list(new_df_pd.iloc[:,2])

for i in sku:
    white_sku.append(i.replace('-','-WA-'))
    yellow_sku.append(i.replace('-','-YA-'))
    
    
new_df_pd['white_sku'] = white_sku
new_df_pd['yellow_sku'] =yellow_sku


new_df_pd = new_df_pd[new_df_pd['SKU']!='PD0081'].reset_index()
new_df_pd.columns
new_df_pd = new_df_pd.ix[:,[ 'Type', 'SKU item_sku', 'Title', 'Product Description',
       'standard_price', 'SKU', 'sub_category', 'strip_category', 'main_title', 'description',
       'white_sku', 'yellow_sku']]

#new_df_pd = new_df_pd.iloc[:,[3,4,5,6,10,13,14,15,16,17]]
no_of_categories = no_of_categories[no_of_categories.index!='PD0081']
#new_df_pd['count'] = no_of_categories
#del new_df_pd['count']
count = list(no_of_categories)
count = [0] + count



