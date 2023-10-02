import email
from email import message
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password

email, password = account_info()

post="It's Nikita"

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

driver.get('https://www.facebook.com/')

email_xpath = '//*[@id="email"]'
password_xpath = '//*[@id="pass"]'


time.sleep(2)

driver.find_element_by_xpath(email_xpath).send_keys(email)
time.sleep(2)
driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(2)
pyautogui.hotkey('enter')



