#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 20:54:52 2017

@author: harshal
"""
#import numpy as np
#import pandas as pd
#
#data = pd.read_csv("/home/harshal/Documents/pythonSelenium/env/data.csv")
#
#sku_list = list(data.iloc[:,1])
#master_sku = []
#category =[]
#category_diamond =[]
#split_sku =[]
#for i in sku_list:
#    j = i.split('-')
#    split_sku.append(j)
#    master_sku.append(j[0])
#        
#category =[]
#for j in split_sku:
#    try:
#        if j[1]=='WA':
#            category.append('White')
#        elif j[1] == 'YA':
#            category.append('Yellow')
#        else:
#            category.append('')
#    except:
#        category.append('')
#    
#category_diamond=[]
#for j in split_sku:
#    try:
#        if j[1] == 'DAM' or j[2] == 'DAM':
#            category_diamond.append('Amethyst')
#        elif j[1] == 'DAQ' or j[2] == 'DAQ':
#            category_diamond.append('Aquamarine')
#        elif j[1] == 'DBT' or j[2] == 'DBT':
#            category_diamond.append('Blue Topaz')
#        elif j[1] == 'DCT' or j[2] == 'DCT':
#            category_diamond.append('Citrine')
#        elif j[1] == 'DGA' or j[2] == 'DGA':
#            category_diamond.append('Green Amethyst')
#        elif j[1] == 'DGT' or j[2] == 'DGT':
#            category_diamond.append('Garnet')
#        elif j[1] == 'DLCE' or j[2] == 'DLCE':
#            category_diamond.append('Lab Created Emerald')
#        elif j[1] == 'DLCR' or j[2] == 'DLCR':
#            category_diamond.append('Lab Created Ruby')
#        elif j[1] == 'DLCS' or j[2] == 'DLCS':
#            category_diamond.append('Lab Created Sapphire')
#        elif j[1] == 'DPD' or j[2] == 'DPD':
#            category_diamond.append('Peridot')
#        elif j[1] == 'DPT' or j[2] == 'DPT':
#            category_diamond.append('Pint Topaz')
#        elif j[1] == 'DSQ' or j[2] == 'DSQ':
#            category_diamond.append('Smokey Quartz')
#        else:
#            category_diamond.append('')
#    except:
#        category_diamond.append('')
#    
#    
#    
#len(category_diamond)
#len(category)
#data['SKU'] = master_sku
#data['category'] = category
#data['sub_category'] = category_diamond

import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chromedriver = "/home/harshal/Documents/pythonSelenium/env/selenium/webdriver/drivers/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get('http://ornaitjewels.com/')
#time.sleep(0.3)
login = driver.find_element_by_css_selector('body > header > div.navbar__login.hidden-sm-down > div > div > div:nth-child(2) > ul > li:nth-child(2) > a')
login.click()
userid = driver.find_element_by_css_selector('#id_username')
userid.send_keys("admin@admin.com")
password = driver.find_element_by_css_selector('#id_password')
password.send_keys("admin")
login = driver.find_element_by_css_selector("body > div.container.maincontent > div > div > div.col-md-6.login__form > form > div > div > button")
login.click()
#dashboard= driver.find_element_by_css_selector("body > header > div.navbar__login.hidden-sm-down > div > div > div:nth-child(2) > ul > li:nth-child(1) > a")
#dashboard.click()
#new_df = new_df.reset_index()
new_df = variant_df.copy(True)
for i in range(len(new_df['SKU'])):
    driver.get('http://ornaitjewels.com/dashboard/')
    products = driver.find_element_by_css_selector("#first > ul > li:nth-child(1) > a")
    products.click()
    
    plus_button = driver.find_element_by_css_selector('body > div.subheader.top-nav > div > div > a > svg > path:nth-child(1)')
    plus_button.click()
    time.sleep(0.3)
    #wait = WebDriverWait(driver, 10)
    
    pendant = driver.find_element_by_css_selector('#modal-product-class > div > form > div:nth-child(2) > div > p:nth-child(3) > label')
    pendant.click()
    
    create_new = driver.find_element_by_css_selector('#modal-product-class > div > form > div:nth-child(3) > div > button')
    create_new.click()
    
    name = driver.find_element_by_css_selector('#id_name')
    name.send_keys(new_df.ix[i,'main_title'])
    
    description = driver.find_element_by_css_selector('#id_description')
    description.send_keys(new_df.ix[i,'description'])
    
    price = driver.find_element_by_css_selector('#id_price')
    price.send_keys(str(new_df.ix[i,'standard_price']))
    
    driver.find_element_by_xpath('//li//input').click()
    driver.find_element_by_xpath('//li[contains(text(),"Pendants")]').click()
#    category_pendant = driver.find_element_by_xpath('//*[@id="select2-id_categories-result-rtqb-6"]')
#    category_pendant.click()
    
    create_new = driver.find_element_by_css_selector('#form-product > div.card-action.right-align > button')
    create_new.click()
    time.sleep(0.2)
    
    for j in range(2):
        if j == 0:
            x = 5
        else:
            x = 6
        variants = driver.find_element_by_css_selector('body > main > div > div.row > div > ul > li:nth-child(2) > a')
        variants.click()
        #### ADD
        driver.find_element_by_css_selector('#variants > form > div.data-table-header-action > a.btn-data-table.btn-show-when-unchecked.btn-flat').click()
        variant_name = driver.find_element_by_css_selector('#id_name')
        variant_name.send_keys(new_df_pd.ix[i,x+2])
        #### DIAMOND
        driver.find_element_by_xpath('//*[@id="form-variant"]/div[1]/div/div[1]/div[2]/div/div/input').click()
        time.sleep(0.2)
        driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[2]/div/div/ul/li[2]').click()
        
        ################## GEMSTONE
        driver.find_element_by_css_selector('#form-variant > div.card-content > div > div.col.s12.m8 > div:nth-child(3) > div > div > input').click()
        time.sleep(0.2)
        driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[3]/div/div/ul/li['+str(g)+']')
        
        ####### Type Of GOLD
        driver.find_element_by_css_selector('#form-variant > div.card-content > div > div.col.s12.m8 > div:nth-child(4) > div > div > input').click()
        time.sleep(0.2)
        if x==5:
            driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[4]/div/div/ul/li['+str(3)+']').click()
        else:
            driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[4]/div/div/ul/li['+str(4)+']').click()
        sku = driver.find_element_by_css_selector('#id_sku')
        sku.send_keys(new_df_pd.ix[i,x])
        ### create
        driver.find_element_by_css_selector('#form-variant > div.card-action.right-align > button').click()
    
    #driver.quit()
