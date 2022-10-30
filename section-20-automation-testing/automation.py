from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
  
service = Service(executable_path='./chromedriver_linux64/chromedriver')
  
chrome_browser = webdriver.Chrome(service=service)

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com')

print('Selenium Easy - Best Demo website to practice Selenium Webdriver Online' in chrome_browser.title)

button = chrome_browser.find_element(By.CLASS_NAME, 'btn-success')
print(button)

# btn btn-success btn-outline-rounded green