"""
this capstone projet for purpose to summary to everything we have seen in automation and web scraping , so in this
projet we will search in a website zillow for house for rent so we select the criteria and after that we got the
result of this reasearch , this result will be fulffiled in a form and after that converted in a sheet and finaly
send to client each day.to achieve this we should use selenuim beatufill soup ...

"""
from operator import contains

import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from dotenv import load_dotenv


URL="https://appbrewery.github.io/Zillow-Clone/"
google_Forme="https://docs.google.com/forms/d/e/1FAIpQLSd_smJxfySit28E60VNVtBvTlh0OCwPe_5-r550AF53heAMbw/viewform?usp=header"
data="https://docs.google.com/forms/d/1wVhxpPej0c9d834BZHtXYduGaq4X9Fw-7YCMr5o5S8g/edit#responses"


#using beautifull soup to scramp into a website and get information :link price and address of the property
load_dotenv()
EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")

prices=[]
addresses=[]
House=[]

Result_website=requests.get(URL)
soup=BeautifulSoup(Result_website.text,"html.parser")

####link
listing=soup.find_all("a",attrs={"tabindex":"0"})

#for link in listing:
#    links.append(link.get("href"))

links=[link.get("href") for link in listing]

####price
prices_list=soup.find_all("span",attrs={"data-test": "property-card-price"})
for price in prices_list:
    pri=price.get_text().strip("+/mo").replace("+ 1 bd","").replace("+ 1bd","")
    prices.append(pri)
####address
address_list=soup.find_all("address")
addresses=[addr.get_text(strip=True) for addr in address_list]

# build a dictionnary with adresse, price and link

for i in range(len(address_list)):

    House.append(
        {'addr':addresses[i],
         'price':prices[i],
         'link':links[i]
        }
    )


# filtrer the information about the rent and put it in google form  using seleniumm to fulffiled the form

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_option)


for element in House:
    driver.get(google_Forme)
    addresse_form=driver.find_element(By.CSS_SELECTOR,value='input[jsname="YPqjbf"]')
    addresse_form.send_keys(element['addr'])
    time.sleep(5)

    price_form=driver.find_element(By.CSS_SELECTOR,value='input[aria-labelledby="i6 i9"]')
    price_form.send_keys(element['price'])
    time.sleep(5)

    price_form = driver.find_element(By.CSS_SELECTOR, value='input[aria-labelledby="i11 i14"]')
    price_form.send_keys(element['link'])
    time.sleep(5)

    driver.find_element(By.XPATH,'//span[text()="Envoyer"]/ancestor::div[@role="button"]').click()
    print("succefull!")


print("we finished the collect of data in the form")

# acceed to data in google form and transfer this data into a sheet

# it's not possible to connect to google form via selenium
driver.get(data)

driver.find_element(By.CSS_SELECTOR,value="div.rW8Rhb").click()
# Attendre le champ email
try:
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"identifierId")))
    email_field.send_keys(EMAIL)
    email_field.send_keys(Keys.ENTER)
except Exception  as e:
    print("can not type the adresse email!")


# Attendre mot de passe
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
)
"""password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(3)
loging_access=driver.find_element(By.CSS_SELECTOR,value="input[type='email']")
loging_access.send_keys(EMAIL)
loging_access.send_keys(Keys.ENTER)
time.sleep(3)
password_form=driver.find_element(By.CSS_SELECTOR,value="input[type='password']")
password_form.send_keys(PASSWORD)
time.sleep(3)"""

driver.find_element(By.CSS_SELECTOR,value="span[jsname='V67aGc']").click()
response=driver.find_element(By.CSS_SELECTOR,value="div.a6yTpb")
response.click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[contains(text(),'Lien vers Sheets')]").click()
driver.find_element(By.XPATH,"//span[contains(text(),'Créer')]").click()
