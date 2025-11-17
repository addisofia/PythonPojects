from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time

load_dotenv()
URL = os.getenv("URL")
USR = os.getenv("USR")
PWD = os.getenv("PWD")


class Instagram_Followers():
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.implicitly_wait(10)

    def login(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),"
                                                             "'Refuser les cookies optionnels')]"))).click()
        except Exception as e:
            print("no cookies to approve or refuse !")

        username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
        username.send_keys(USR)

        password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
        password.send_keys(PWD)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Se connecter')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Plus tard')]"))).click()

    def scroll_down(self, scrolls):
        self.driver.get("https://www.instagram.com/chefsteps/")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'followers')]"))).click()
        time.sleep(5)

        # find the scroll down
        try:
            scroll_box = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))
            time.sleep(2)
        except Exception as e:
            print("we do not find scroll down")
            return

        last_height = 0
        for i in range(scrolls):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
            time.sleep(2)

               # Optionnel : vérifier si le scroll a chargé plus de followers
            new_height = self.driver.execute_script("return arguments[0].scrollTop", scroll_box)
            if new_height == last_height:
                break
            last_height = new_height



    def follow(self):
        followers_list = self.driver.find_elements(By.XPATH, "//div[contains(text(),'Suivre')]")
        print(f"number of users that we will follow is : {len(followers_list)}")

        for follower in followers_list:
            try:
                follower.click()
                print("got it , you followed a new user !")
                time.sleep(5)

            except Exception as e:
                print("sorry we can not follow this new user!")


Bot = Instagram_Followers()
Bot.login()
Bot.scroll_down(2)
Bot.follow()

