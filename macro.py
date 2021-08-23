#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

my_id="leetwon134@naver.com"
my_pw=""
spt=2

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# driver=webdriver.Chrome("/usr/local/bin/chromedriver",options=chrome_options)
driver=webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("http://naver.com")

#xpath='//태그[@속성="속성값"]'
xpath='//a[@class="link_login"]'
driver.find_element_by_xpath(xpath).click()
time.sleep(spt)

pyperclip.copy(my_id)
xpath2='//input[@id="id"]'
driver.find_element_by_xpath(xpath2).send_keys(Keys.COMMAND,'v')
# time.sleep(spt)

pyperclip.copy(my_pw)
xpath3='//input[@id="pw"]'
driver.find_element_by_xpath(xpath3).send_keys(Keys.COMMAND,'v')
# time.sleep(spt)

xpath4='//input[@id="log.login"]'
driver.find_element_by_xpath(xpath4).click()
