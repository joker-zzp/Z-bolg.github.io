# /usr/bin/python3
# -*- encoding: utf-8 -*-
#
# @filename      : selenium.py
# @author        : joker-zzp
# @created       : Tue Mar 26 2019 15:21:46 GMT+0800 (中国标准时间)
# @last-modified : Tue Mar 26 2019 21:28:52 GMT+0800 (中国标准时间)
# @description   : 项目描述
#

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 声明驱动对象
# driver = webdriver.Firefox("C:/Program Files/Mozilla Firefox/geckodriver.exe")

driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
driver.maximize_window()

driver.get('https://www.baidu.com')

print("登录时间60秒")
time.sleep(10)

# for i in range(9):
#     time.sleep(1)
#     print("开始倒计时：", 9 - i)

# while True:
#     try:
#         # time.sleep(0.3)
#         # driver.find_element(By.NAME, 'amount').clear()
#         # driver.find_element(By.NAME, 'amount').send_keys('400')
#         # time.sleep(0.3)
#         # driver.find_element(By.CLASS_NAME, 'bg-buy').click()
#         # print("买入成功！ 时间：", time.time())
#     except Exception:
#         print("页面找不到元素，时间：", time.time())
#         driver.refresh()
#         time.sleep(1.5)
        
driver.close()
