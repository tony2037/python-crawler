import requests
from selenium import webdriver

import time

res = requests.get('https://www.youtube.com')
print(res.text)
print('print out youtube\'s html by requests.get(\'url\')')

for i in range(1,6):
    print('#')

chromedriverPath="D:\Atom workspace\Python\chrome driver\chromedriver.exe"
#It's the path of chromedriver
driver = webdriver.Chrome(chromedriverPath)
#Construct a webdriver.chrome()
driver.get('https://www.youtube.com')
source = driver.page_source
#Getting the page's source via webdriver
print(source)

time.sleep(10)

print('gonna click')
driver.find_element_by_link_text('登入').click()
