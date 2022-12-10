import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from csv import writer
giris= input("enter the product word to be searched: ") #words to search
options = webdriver.ChromeOptions() #webdriver Chrome options entry
options.add_argument('headless')#code required for window not to open
driver = webdriver.Chrome(options=options)
driver.get("https://www.trendyol.com/")#Driver get open the window wbsite url
driver.find_element(By.ID,"Combined-Shape").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/input").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/input").send_keys(giris)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/i").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[2]").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[2]/select/option[7]").click()
elements=driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/div[1]/div")
name = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[3]/div[1]/a/div[2]/div[1]/div")
for name in elements:
    print(name.text)
sleep(20)

