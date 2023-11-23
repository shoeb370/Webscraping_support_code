# pip install selenium
# pip install openpyxl
import openpyxl 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url_)
user = driver.find_element(By.ID,'username').send_keys('shoebahmed370@outlook.com')
driver.find_element(By.XPATH,"//input[@class='class_name']").clear()
source  = BeautifulSoup(driver.page_source)
search_section = source.find('div', {'class': "search-results-container"})
matching_elements = soup.find_all(text=lambda text: text and "Dell Latitude" in text)

table1 = source.find('table')
if table1 != None:
    df_spec_temp = pd.read_html(str(table1))[0]

    
