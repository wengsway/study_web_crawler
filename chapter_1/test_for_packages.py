#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/8/2019 7:55 PM 
# File  : test_for_packages.py
# IDE   : PyCharm

import tesserocr
from PIL import Image
from selenium import webdriver
from bs4 import BeautifulSoup


# Part 1: test selenium
# prepare the option for the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('headless')

# start chrome browser
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.baidu.com')
print(browser.current_url)
browser.quit()


# Part 2: test beautifulsoup4
soup = BeautifulSoup('<p>Hello<p>', 'lxml')
print(soup.p.string)


# Part 3: test tesserocr
# method one: use image_to_text
image = Image.open('chapter_1/python3webspider.png')
print(tesserocr.image_to_text(image))

# method two: use file_to_text
print(tesserocr.file_to_text('chapter_1/python3webspider.png'))
