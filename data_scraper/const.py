# TinderBot - const.py
# Version 1.0
# Created by Cyanox - https://github.com/Cyanox
# 02/10/2022

from selenium.webdriver.chrome.options import Options

options = Options()

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
# OPTIONS.add_argument(f'user-agent={user_agent}')
# options.add_argument(r'--user-data-dir=C:\Users\alexi\AppData\Local\Google\Chrome\User Data')
# options.add_argument(r'--profile-directory=Default')

options.add_argument("--disable-extensions --disable-gpu --disable-dev-shm-usage --disable")
# OPTIONS.add_experimental_option('excludeSwitches', ['enable-logging'])

# OPTIONS.add_argument("--no-first-run --no-service-autorun --password-store=basic")

options.add_argument("window-size=1920,1080")
options.add_argument("start-maximised")

# OPTIONS.add_argument('--disable-blink-features=AutomationControlled')
# OPTIONS.add_experimental_option('useAutomationExtension', False)
# OPTIONS.add_experimental_option("excludeSwitches", ['enable-automation']);

# OPTIONS.add_argument("--headless")
