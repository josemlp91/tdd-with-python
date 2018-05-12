from selenium import webdriver 

browser =  webdriver.Chrome("/usr/local/bin/chromedriver")

try:
    browser.get("http://localhost:8000")
except:
    pass

assert  'Django' in browser.title

