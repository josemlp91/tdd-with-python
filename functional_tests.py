from selenium import webdriver 

browser = webdriver.Firefox()

try:
    browser.get("http://localhost:8000")
except:
    pass

assert  'Django' in browser.title

