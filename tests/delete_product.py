#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:48:21 2017

@author: harshal
"""

#sites = ['http://ornaitjewels.com/dashboard/products/134/update/',
#'http://ornaitjewels.com/dashboard/products/135/update/',
#'http://ornaitjewels.com/dashboard/products/136/update/',
#'http://ornaitjewels.com/dashboard/products/137/update/',
#'http://ornaitjewels.com/dashboard/products/138/update/',
#'http://ornaitjewels.com/dashboard/products/139/update/',
#'http://ornaitjewels.com/dashboard/products/140/update/',
#'http://ornaitjewels.com/dashboard/products/141/update/',
#'http://ornaitjewels.com/dashboard/products/142/update/',
#'http://ornaitjewels.com/dashboard/products/143/update/',
#'http://ornaitjewels.com/dashboard/products/144/update/',
#'http://ornaitjewels.com/dashboard/products/145/update/',
#'http://ornaitjewels.com/dashboard/products/146/update/',
#'http://ornaitjewels.com/dashboard/products/147/update/']

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

for i in range(200,219):
    site = 'http://ornaitjewels.com/dashboard/products/'+str(i)+'/update/'
    driver.get(site)
    driver.find_element_by_css_selector('body > div.subheader.top-nav > div > a > svg').click()
    time.sleep(0.2)
    driver.find_element_by_css_selector('#context-menu > li:nth-child(2) > a').click()
    time.sleep(0.2)
    driver.find_element_by_css_selector('#base-modal > form > div.modal-footer > button').click()
#    except:
#        continue