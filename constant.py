from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:/Users/crenauro/Documents/selenium_training/chromedriver.exe")
driver = webdriver.Chrome(service=s)

fbUrl = "https://www.facebook.com/"
screenshot_path = "C:/Users/crenauro/Documents/selenium_training/"

username ="hello@gmail.com"
password = "6qLyX2huW"