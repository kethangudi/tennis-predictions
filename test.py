from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://vaibhavgurunathan.github.io/")
time.sleep(3) 

# links = driver.find_element(By.TAG_NAME, "a")
# links = driver.find_elements(By.TAG_NAME, "a")
# for link in links:
#     #is_href = link.get_attribute("href")
#     #if is_href:
#     link.click()
#     title = driver.title
#     print(title,"\n")
#     driver.back()
#     # else:
#     #     print("Fail\n")

#find all links
has_href = driver.find_elements(By.TAG_NAME, "a")
for link in has_href:
    href = link.get_attribute("href")
    if href:
        print(href)
    else:
        print("Fail")

driver.quit()