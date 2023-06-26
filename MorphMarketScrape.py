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

#errors to log where scrape failed
errors = []
# Create a new instance of the Firefox sdriver
#os.chdir(r'/Users/hconner/')  # /Users/hconner/Downloads/chromedriver_mac64 (1) 2/chromedriver
driver = webdriver.Chrome(executable_path='/Users/hconner/Downloads/chromedriver_mac64 (1) 2/chromedriver')

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
data = pd.DataFrame(columns=['AnimalType1', 'AnimalType2','Info' ,'About1', 'About2', 'Seller'])

# Get relevant data gets all the data on the webpage for a particular amphibian

def getRelevantData():
                                                 #//*[@id="snake-page"]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/h1
    animal_type1 = driver.find_element(By.XPATH, '//*[@id="snake-page"]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/h1').text
    animal_type2 = driver.find_element(By.XPATH, '//*[@id="snake-page"]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').text
                                                #//*[@id="snake-page"]/div/div/div/div[2]/div[2]/div
    animal_info = driver.find_element(By.XPATH, '//*[@id="snake-page"]/div/div/div/div[2]/div[2]/div').text
    animal_about1 = driver.find_element(By.XPATH,'//*[@id="snake-page"]/div/div/div/div[2]/div[1]').text
                                                  #//*[@id="snake-page"]/div/div/div/div[2]/div[1]/div[3]/div[1]
    animal_about2 = driver.find_element(By.XPATH, '//*[@id="snake-page"]/div/div/div/div[2]/div[1]/div[3]/div[1]').text
    seller = driver.find_element(By.XPATH, '//*[@id="snake-page"]/div/div/div/div[2]/div[2]/div/div[1]/div[6]').text
    return([animal_type1, animal_type2, animal_info, animal_about1, animal_about2, seller])

for page in range(0,numOfP):
    for i in range(1, 25):
                # //*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[1]/div[2]/picture/img
        xpath = '//*[@id="root"]/div[2]/div[2]/div/div[6]/div[3]/div/div[1]/a[{}]/div[2]/picture/img'.format(i)
        try:
            driver.find_element(By.XPATH, xpath).click()
            try:
                data.loc[len(data)] = getRelevantData()
                driver.back()
            except Exception as e:
                errors.append(i)
                driver.back()
        except Exception as e:
            errors.append(e)
    driver.find_element(By.CSS_SELECTOR, '#root > div.PD8nHTdml1ZBT90vCA6l > div.F8dpc6zxp2_Y4GgkBu1K.mainWrapper > div > div.JnHtrfiYyDbC27y8oB8a > div.sAtvmyDfu3pfgUuvn0ww > div > div.Ac9cgD8VuNGFRxtfonUP.seB8J1vqvLrPSoVxmSFe > div > div > a:nth-child(4) > div > svg').click()


    print(page)

data = data.drop_duplicates()

os.chdir(r'/Users/hconner/AmphibianData')
data.to_csv(name)

#########################################
# Types of Amphibians
########################################

# //*[@id="animals_by_tag"]/div[3]/div/div/div/h5/a
# //*[@id="animals_by_tag"]/div[4]/div/div/div/h5/a


