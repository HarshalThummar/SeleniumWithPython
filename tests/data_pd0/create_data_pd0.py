#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 00:28:26 2017

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
#data_mpd = data.iloc[index_mpd,:].reset_index()
#
#split_sku_mpd = split_sku[index_mpd[0]:index_mpd[-1]+1]
#
#category =[]
#for i in split_sku_mpd:
#    try:
#        if i[1]=='WA' or i[2]=='WA':
#            category.append('White')
#        elif i[1] == 'YA' or i[2] =='YA':
#            category.append('Yellow')
#        else:
#            category.append('')
#    except:
#        category.append('')
#
#
#data_mpd['category'] = category
#
#category_diamond=[]
#for j in split_sku_mpd:
#    try:
#        if j[2] == 'DAM':
#            category_diamond.append('Amethyst')
#        elif j[2] == 'DAQ':
#            category_diamond.append('Aquamarine')
#        elif j[2] == 'DBT':
#            category_diamond.append('Blue Topaz')
#        elif j[2] == 'DCT':
#            category_diamond.append('Citrine')
#        elif j[2] == 'DGA':
#            category_diamond.append('Green Amethyst')
#        elif j[2] == 'DGT':
#            category_diamond.append('Garnet')
#        elif j[2] == 'LCE':
#            category_diamond.append('Lab Created Emerald')
#        elif j[2] == 'LCR':
#            category_diamond.append('Lab Created Ruby')
#        elif j[2] == 'LCS':
#            category_diamond.append('Lab Created Sapphire')
#        elif j[2] == 'DPD':
#            category_diamond.append('Peridot')
#        elif j[2] == 'DPT':
#            category_diamond.append('Pint Topaz')
#        elif j[2] == 'DSQ':
#            category_diamond.append('Smokey Quartz')
#        else:
#            category_diamond.append('')
#    except:
#        category_diamond.append('')

################################################## PD

data_pd2 = data.iloc[index_pd2,:].reset_index()

split_sku_pd2 = split_sku[index_pd2[0]:index_pd2[-1]+1]

category =[]
for i in split_sku_pd2:
    try:
        if i[1]=='WB':
            category.append('White')
        elif i[1] == 'YB':
            category.append('Yellow')
        elif i[1] == 'SL':
            category.append('Silver')
        else:
            category.append('')
    except:
        category.append('')


data_pd2['category'] = category

#no_of_categories = new_df_pd2.groupby('SKU').size()

category_diamond=[]
for j in split_sku_pd2:
    try:
        if j[-1] == 'AM':
            category_diamond.append('Amethyst')
        elif j[-1] == 'AQ':
            category_diamond.append('Aquamarine')
        elif j[-1] == 'BT':
            category_diamond.append('Blue Topaz')
        elif j[-1] == 'CT':
            category_diamond.append('Citrine')
        elif j[-1] == 'GT':
            category_diamond.append('Garnet')
        elif j[-1] == 'OP':
            category_diamond.append('Olap')
        elif j[-1] == 'PD':
            category_diamond.append('Peridot')
        elif j[-1] == 'PT':
            category_diamond.append('Pink Topaz')
        elif j[-1] == 'SQ':
            category_diamond.append('Smokey Quartz')
        elif j[-1] == 'EM':
            category_diamond.append('Emerald')
        elif j[-1] == 'RB':
            category_diamond.append('Ruby')
        elif j[-1] == 'SP':
            category_diamond.append('Sapphire')
        elif j[-1] == 'TZ':
            category_diamond.append('Tanzanite')
        else:
            category_diamond.append('')
    except:
        category_diamond.append('')
        
data_pd2['sub_category'] = category_diamond

strip_category =[]
for i in split_sku_pd2:
    try:
        if i[1]=='WB' or i[1] == 'YB' or i[1] == 'SL':
            strip_category.append(i[0]+'-'+i[-1])
        else:
            strip_category.append(i[0]+'-'+i[-1])
    except:
        strip_category.append('')
        
        
data_pd2['strip_category'] = strip_category

new_df_pd2 = data_pd2.drop_duplicates(subset =  ['strip_category'],keep="first")

title = list(new_df_pd2['Title'])
main_title =[]
for i in title:
    if 'Amethyst' in i:
        main_title.append(i.replace(' Amethyst ',' Gemstone '))
    elif 'Aquamarine' in i:
        main_title.append(i.replace(' Aquamarine ',' Gemstone '))
    elif 'Blue Topaz' in i:
        main_title.append(i.replace(' Blue Topaz ',' Gemstone '))
    elif 'Citrine' in i:
        main_title.append(i.replace(' Citrine ',' Gemstone '))
    elif 'Garnet' in i:
        main_title.append(i.replace(' Garnet ',' Gemstone '))
    elif 'Emerald' in i:
        main_title.append(i.replace(' Emerald ',' Gemstone '))
    elif 'Ruby' in i:
        main_title.append(i.replace(' Ruby ',' Gemstone '))
    elif 'Sapphire' in i:
        main_title.append(i.replace(' Sapphire ',' Gemstone '))
    elif 'Peridot' in i:
        main_title.append(i.replace(' Peridot ',' Gemstone '))
    elif 'Pink Topaz' in i:
        main_title.append(i.replace(' Pink Topaz ',' Gemstone '))
    elif 'Smokey Quartz' in i:
        main_title.append(i.replace(' Smokey Quartz ',' Gemstone '))
    elif 'Tanzanite' in i:
        main_title.append(i.replace(' Tanzanite ',' Gemstone '))
    elif 'Opal' in i:
        main_title.append(i.replace(' Opal ',' Gemstone '))
    else:
        main_title.append('')
        

        
main_title2 =[]
for i in main_title:
    if 'Silver' in i:
        main_title2.append(i.replace('Sterling Silver', 'Silver and 14K Gold'))
    elif 'Yellow Gold' in i:
        main_title2.append(i.replace('14k Yellow Gold', 'Silver and 14K Gold'))
    elif 'White Gold' in i:
        main_title2.append(i.replace('14k White Gold','Silver and 14k Gold' ))
    else:
        main_title2.append('')


new_df_pd2['main_title'] = main_title2


description  = list(new_df_pd2['Product Description'])
main_descrip = []
for i in description:
    if 'Amethyst' in i:
        main_descrip.append(i.replace(' Amethyst ',' Gemstone '))
    elif 'Aquamarine' in i:
        main_descrip.append(i.replace(' Aquamarine ',' Gemstone '))
    elif 'Blue Topaz' in i:
        main_descrip.append(i.replace(' Blue Topaz ',' Gemstone '))
    elif 'Citrine' in i:
        main_descrip.append(i.replace(' Citrine ',' Gemstone '))
    elif 'Garnet' in i:
        main_descrip.append(i.replace(' Garnet ',' Gemstone '))
    elif 'Emerald' in i:
        main_descrip.append(i.replace(' Emerald ',' Gemstone '))
    elif 'Ruby' in i:
        main_descrip.append(i.replace(' Ruby ',' Gemstone '))
    elif 'Sapphire' in i:
        main_descrip.append(i.replace(' Sapphire ',' Gemstone '))
    elif 'Peridot' in i:
        main_descrip.append(i.replace(' Peridot ',' Gemstone '))
    elif 'Pink Topaz' in i:
        main_descrip.append(i.replace(' Pink Topaz ',' Gemstone '))
    elif 'Smokey Quartz' in i:
        main_descrip.append(i.replace(' Smokey Quartz ',' Gemstone '))
    elif 'Opal' in i:
        main_descrip.append(i.replace(' Opal ',' Gemstone '))
    elif 'Tanzanite' in i:
        main_descrip.append(i.replace(' Tanzanite ',' Gemstone '))
    else:
        main_descrip.append('')
    
for i in range(len(main_descrip)):
    if 'Ruby' in main_descrip[i]:
        main_descrip[i] = main_descrip[i].replace('Ruby','Gemstone')
    
#for i in range(len(main_descrip)):
#    if 'sterling Silver'
    
    
new_df_pd2['description'] = main_descrip

white_sku = []
yellow_sku = []
silver_sku = []
sku = list(new_df_pd2.ix[:,'strip_category'])

for i in sku:
    white_sku.append(i.replace('-','-WB-'))
    yellow_sku.append(i.replace('-','-YB-'))
    silver_sku.append(i.replace('-','-SL-'))
    
new_df_pd2['white_sku'] = white_sku
new_df_pd2['yellow_sku'] =yellow_sku
new_df_pd2['silver_sku'] = silver_sku

#new_df_pd = new_df_pd[new_df_pd['SKU']!='PD0081'].reset_index()
new_df_pd2.columns
new_df_pd2 = new_df_pd2.ix[:,[ 'Type', 'SKU item_sku', 'Title', 'Product Description',
       'standard_price', 'SKU', 'sub_category', 'strip_category', 'main_title', 'description',
       'white_sku', 'yellow_sku','silver_sku']]
no_of_categories = new_df_pd2.groupby('SKU').size()

#new_df_pd = new_df_pd.iloc[:,[3,4,5,6,10,13,14,15,16,17]]
#no_of_categories = no_of_categories[no_of_categories.index!='PD0081']
#new_df_pd['count'] = no_of_categories
#del new_df_pd['count']
#count = list(no_of_categories)

count =[]
for i in list(no_of_categories):
    count.append(int(i))

count = [0] + count


title = list(new_df_pd2['Title'])
title_new = []

for i in title:
    title_new.append(i.replace('Sterling Silver' , 'Silver and Gold'))
    
new_df_pd2['Title'] = title_new
new_df_pd2  = new_df_pd2.reset_index()