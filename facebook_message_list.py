# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:33:06 2020

@author: Tejas
"""
from selenium import webdriver
import time
import logindata
from datetime import date

today = date.today()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome('F:\Channel\webdriver\chromedriver.exe', chrome_options=options)
time.sleep(1)

driver.get('http://facebook.com')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="email"]').send_keys(logindata.USERNAME)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(logindata.PASSWORD)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
time.sleep(1)


while True:
    
    opt = input('Enter:\n1)Message\n2)Friend Request\n3)Notifications\n') 
    
    if opt=='1':         
        '''Message Section'''
        driver.find_element_by_xpath('//*[@id="u_0_e"]/a/div').click()
        time.sleep(3)
        
        message = driver.find_element_by_css_selector('ul.jewelContent')
        
        MsgList = message.find_elements_by_tag_name('strong')
        
        Msgdate = message.find_elements_by_css_selector('abbr.timestamp')
        
        for name,msgDt in zip(MsgList,Msgdate):
            print('\n',format(msgDt.text))
            print((name.find_element_by_tag_name('span').text))
       
    if opt=='2':
        '''Friends List'''   
        driver.find_element_by_xpath('//*[@id="fbRequestsJewel"]/a/div').click()
        time.sleep(3)
        
        friends = driver.find_element_by_css_selector('ul.jewelItemList')
        
        frndList = friends.find_elements_by_css_selector('span.fsl')
        
        for li in frndList:
            print(li.text)
    
    if opt=='3':
        '''Notifications Section'''
        driver.find_element_by_xpath('//*[@id="fbNotificationsJewel"]/a/div').click()
        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="u_0_g"]').click()


    
