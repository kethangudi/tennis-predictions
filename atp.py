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
#driver = webdriver.Chrome(executable_path='/home/kgudi/tennis/atp/chromedriver',options=options)
#PATH = "C:\Users\gudik\atp\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
driver.get("https://www.atptour.com/en/players/")
#driver.get("https://app.universaltennis.com/profiles/3478")
time.sleep(3)

col=[]
with open('names.csv', mode ='r')as file:
   
  # reading the CSV file
    csvFile = csv.reader(file)
    #desired_queries = csvFile
    count = 0
    for query in csvFile:
        time.sleep(3)
        url = []
        search = driver.find_element(By.CLASS_NAME,'atp-search')
        search.click()

       
        search2 = driver.find_element(By.CLASS_NAME,'search')
        #search2.click()
        driver.execute_script("arguments[0].click();", search2)
        search2.send_keys(query)
        time.sleep(3)

        clique = driver.find_element(By.CLASS_NAME,'predictive-result-title')
        clique.click()
        #search2.send_keys(Keys.RETURN)
        time.sleep(3)

        url.append(driver.current_url[35:len(driver.current_url)-9])
        col.append(url)
        time.sleep(3)
        driver.get("https://www.atptour.com/en/players/")
        with open ('links.csv','w',newline = '') as csvfile:
          my_writer = csv.writer(csvfile)
          my_writer.writerows(col)

time.sleep(3)
driver.quit()
#with open ('links.csv','w',newline = '') as csvfile:
    #my_writer = csv.writer(csvfile, delimiter = ' ')
   # my_writer.writerows(col)