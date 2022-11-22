# TinderBot - picture_scraper.py
# Version 1.0
# Created by Cyanox - https://github.com/Cyanox
# 02/10/2022

import os
import json
import random
import math

import pickle
import time

import selenium
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from const import options

PATH_DRIVER = os.path.join(os.curdir, '../chromedriver')

def main():
    # Load the categories
    # Set the driver
    driver = webdriver.Chrome(PATH_DRIVER, options=options)
    print('Loading PKL')
    time.sleep(0.1)
    # cookies = pickle.load(open("cookies.pkl", "rb"))
    # for cookie in cookies:
    #     print(cookie)
    #     driver.add_cookie(cookie)

    driver.get('https://tinder.com/app/recs')
    time.sleep(90)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    # Collect urls data
    save_profile_picture(driver)

    driver.quit()

def save_profile_picture(driver):
    while True:
        if WebDriverWait(driver, 90).until(
                EC.presence_of_element_located((
                        By.CSS_SELECTOR, 'div[style*="rgba(16, 224, 132, 0)"] span[style*="invert"]'))):
            print('Like')
        elif WebDriverWait(driver, 90).until(
                EC.presence_of_element_located((
                        By.CSS_SELECTOR, 'div[style*="rgba(253, 84, 108, 0)"] span[style*="none"]'))):
            print('Nope')
        else:
            print('End')
            break


if __name__ == "__main__":
    main()
