from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import datetime
  
# creating the date object of today's date
name = f'data_{datetime.datetime.now().strftime("%H%M_%m%d%Y")}.csv'

# Create a new instance of the Firefox sdriver
os.chdir(r'/Users/hconner/')
driver = webdriver.Chrome()

# Navigate to the Craigslist homepage
driver.get("https://www.morphmarket.com/")


search_bar = driver.find_element(By.XPATH, '//*[@id="mui-2"]')
search_bar.send_keys("amphibians" +  Keys.RETURN)

#//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[3]/div/div/div
numOfPages = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[3]/div/div/div').text
#numOfPages[:11]
#grabbing all numbers
numOfPages = re.findall(r'\d{1,5}', numOfPages) #re.findall(r'of',numOfPages)
#not sure if it is safe to grab the highest or the 2 highest in the list
#probably can grab the last 2 entries

#number of links
numOfP = int(numOfPages[1])
#number of pages needed to loop through for all the links
#numOfP = int(numOfLinks/int(numOfPages[1]))
data = pd.DataFrame(columns=['Info' ,'About1', 'About2'])

#Make a function to click on the image 
#click on page
def getRelevantData():

    animal_info = driver.find_element(By.XPATH, '//*[@id="snake-page"]/div/div/div/div[2]/div[3]/div').text
    animal_about1 = driver.find_element(By.XPATH,'//*[@id="snake-page"]/div/div/div/div[2]/div[1]').text
    animal_about2 = driver.find_element(By.XPATH, '//*[@id="snake-page"]/div/div/div/div[2]/div[2]/div[3]/div[1]').text
    return([animal_info, animal_about1, animal_about2])


def loopThroughPages():
    #links = driver.find_elements(By.XPATH,"//a[@href]")
    #driver.find_elements(By.CLASS_NAME, 'picture')
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[1]/div[1]/picture/img').click()
    #driver.find_element(By.CSS_SELECTOR,('#root > div.PD8nHTdml1ZBT90vCA6l > div.F8dpc6zxp2_Y4GgkBu1K.mainWrapper > div > div.JnHtrfiYyDbC27y8oB8a > div.sAtvmyDfu3pfgUuvn0ww > div > div.qeswiUQAiXWDYjomZK4l.ecDwgWn62vauKo40KZy4 > a:nth-child(1) > div.zw6z68zM9Btssb5Hgh6l > picture > img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #second link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[2]/div[1]/picture/img')).click()
    #get page info
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #third link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[3]/div[1]/picture/img')).click()
    #get page info
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #fourth link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[4]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #fifth link                    //*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[4]/div[1]/picture/img
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[5]/div[1]/picture/img')).click()
    #get page info
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #sixth link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[6]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #seventh link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[7]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #eighth link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[8]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #ninth link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[9]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #tenth link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[10]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #eleventh link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[11]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #twelvth link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[12]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #thirteenth link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[13]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #fourteenth link               //*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[14]/div[1]/picture/img
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[14]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #fifteenth link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[15]/div[1]/picture/img')).click()
    #get page info
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #sixteenth link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[16]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #17 link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[17]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #18 link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[18]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #19 link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[19]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()
    #20 link
    driver.find_element(By.XPATH,('//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[20]/div[1]/picture/img')).click()
    data.loc[len(data)] = getRelevantData()
    driver.back()

    driver.find_element(By.CSS_SELECTOR, '#root > div.PD8nHTdml1ZBT90vCA6l > div.F8dpc6zxp2_Y4GgkBu1K.mainWrapper > div > div.JnHtrfiYyDbC27y8oB8a > div.sAtvmyDfu3pfgUuvn0ww > div > div.Ac9cgD8VuNGFRxtfonUP.seB8J1vqvLrPSoVxmSFe > div > div > a:nth-child(4) > div > svg').click()
    #Write to google drive as csv

    return data

for page in range(0,numOfP):
    loopThroughPages()
    print(page)

data.to_csv(name)
