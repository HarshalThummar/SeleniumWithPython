#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 08:49:11 2017

@author: harshal
"""

import os
from selenium import webdriver

chromedriver = "/home/harshal/Documents/pythonSelenium/env/selenium/webdriver/drivers/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


import os
from selenium import webdriver
import time
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
driver.get('http://ornaitjewels.com/dashboard/')
products = driver.find_element_by_css_selector("#first > ul > li:nth-child(1) > a")
products.click()

driver.get('http://ornaitjewels.com/dashboard/products/116/variants/add/')

driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[3]/div/div/input').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[3]/div/div/ul/li[3]').click()
#driver.find_element_by_xpath('//*[@id="form-variant"]/div[1]/div/div[1]/div[2]/div/div/input').click()
#time.sleep(1)
#driver.find_elements_by_xpath('//*[@id="form-variant"]//div[1]//div//div[1]//div[2]//div//div[contains(text(),"Diamond")]').click()
#print('/html/body/main/div/div/div[1]/div/form/div[1]/div/div[1]/div[3]/div/div/ul/li['+str(2)+']')

driver.quit()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 09:59:18 2017

@author: harshal
"""

import numpy as np
import pandas as pd

data = pd.read_csv("/home/harshal/Documents/pythonSelenium/env/data.csv")

sku_list = list(data.iloc[:,1])
master_sku = []
for i in sku_list:
    j = i.split('-')
    master_sku.append(j[0])
    
data['SKU'] = master_sku