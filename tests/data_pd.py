#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:47:15 2017

@author: harshal
"""

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
#new_df = variant_df.copy(True)
index = 0
for i in range(len(count)-1):
    driver.get('http://ornaitjewels.com/dashboard/')
    products = driver.find_element_by_css_selector("#first > ul > li:nth-child(1) > a")
    products.click()
    
    plus_button = driver.find_element_by_css_selector('body > div.subheader.top-nav > div > div > a > svg > path:nth-child(1)')
    plus_button.click()
    time.sleep(0.3)
    #wait = WebDriverWait(driver, 10)
    
    pendant = driver.find_element_by_css_selector('#modal-product-class > div > form > div:nth-child(2) > div > p:nth-child(4) > label')
    pendant.click()
    
    create_new = driver.find_element_by_css_selector('#modal-product-class > div > form > div:nth-child(3) > div > button')
    create_new.click()
    
    index += count[i]
    name = driver.find_element_by_css_selector('#id_name')
    name.send_keys(new_df_pd.ix[int(index),'main_title'])
    
    description = driver.find_element_by_css_selector('#id_description')
    description.send_keys(new_df_pd.ix[int(index),'description'])
    
    price = driver.find_element_by_css_selector('#id_price')
    price.send_keys(str(new_df_pd.ix[int(index),'standard_price']))
    
    driver.find_element_by_xpath('//li//input').click()
    driver.find_element_by_xpath('//li[contains(text(),"Pendants")]').click()
#    category_pendant = driver.find_element_by_xpath('//*[@id="select2-id_categories-result-rtqb-6"]')
#    category_pendant.click()
    
    create_new = driver.find_element_by_css_selector('#form-product > div.card-action.right-align > button')
    create_new.click()
    time.sleep(0.2)
    
    for j in range(2):
        if j ==0:
            x = -2
        else:
            x = -1

        for k in range(int(count[i+1])):
            if new_df_pd.ix[index+k,'sub_category'] == 'Amethyst':
                g = 13
            if new_df_pd.ix[index+k,'sub_category'] == 'Aquamarine':
                g = 12
            if new_df_pd.ix[index+k,'sub_category'] == 'Blue Topaz':
                g = 11
            if new_df_pd.ix[index+k,'sub_category'] == 'Green Amethyst':
                g = 9
            if new_df_pd.ix[index+k,'sub_category'] == 'Lab Created Emerald'or new_df_pd.ix[index+k,'sub_category'] == 'Emerald' :
                g = 7
            if new_df_pd.ix[index+k,'sub_category'] == 'Lab Created Ruby'or new_df_pd.ix[index+k,'sub_category'] == 'Ruby':
                g = 6
            if new_df_pd.ix[index+k,'sub_category'] == 'Lab Created Sapphire' or new_df_pd.ix[index+k,'sub_category'] == 'Sapphire':
                g = 5
            if new_df_pd.ix[index+k,'sub_category'] == 'Peridot':
                g = 4
            if new_df_pd.ix[index+k,'sub_category'] == 'Pink Topaz':
                g = 3
            if new_df_pd.ix[index+k,'sub_category'] == 'Citrine':
                g = 10
            if new_df_pd.ix[index+k,'sub_category'] == 'Smokey Quartz':
                g = 2
            if new_df_pd.ix[index+k,'sub_category'] == 'Garnet':
                g = 8
                
            variants = driver.find_element_by_css_selector('body > main > div > div.row > div > ul > li:nth-child(2) > a')
            variants.click()
#            time.sleep(0.2)
#            driver.refresh()
#            details = driver.find_element_by_css_selector('body > main > div > div.row > div > ul > li:nth-child(1) > a')
#            details.click()
##            time.sleep(0.2)
#            variants.click()
            ################### ADD
            driver.find_element_by_css_selector('#variants > form > div.data-table-header-action > a.btn-data-table.btn-show-when-unchecked.btn-flat').click()
            variant_name = driver.find_element_by_css_selector('#id_name')
            variant_name.send_keys(new_df_pd.ix[int(index+k),2])
            ################## DIAMOND
            driver.find_element_by_xpath('//*[@id="form-variant"]/div[1]/div/div[1]/div[2]/div/div/input').click()
            time.sleep(0.2)
            driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[2]/div/div/ul/li[2]').click()
            
            ################## GEMSTONE
            driver.find_element_by_css_selector('#form-variant > div.card-content > div > div.col.s12.m8 > div:nth-child(3) > div > div > input').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[3]/div/div/ul/li['+str(g)+']').click()
            time.sleep(0.3)
            #################### Type Of GOLD
            driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[4]/div/div/input').click()
            time.sleep(0.3)
            if x==(-2):
                ##WG
                driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[4]/div/div/ul/li['+str(3)+']').click()
            else:##YG
                driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[4]/div/div/ul/li['+str(4)+']').click()
            sku = driver.find_element_by_css_selector('#id_sku')
            sku.send_keys(new_df_pd.ix[int(index+k),x])
            
            ############## Price
            price = driver.find_element_by_css_selector('#id_price_override')
            price.send_keys(str(new_df_pd.ix[int(index+k),4]))
            
            ############### create
            driver.find_element_by_css_selector('#form-variant > div.card-action.right-align > button').click()
            driver.refresh()
            #driver.quit()
    
