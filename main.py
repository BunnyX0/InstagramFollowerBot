import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "YOUR EMAIL FOR INSTA HERE"
PASSWORD = "YOUR PASSWORD FOR INSTA HERE"
TARGET_ACCOUNT = "THE ACCOUNT NAME YOU WANT TO FOLLOW THIER FOLLOWERS"


chrome_driver_path = "YOUR CHOMRE PATH"
service = Service(chrome_driver_path)

class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(4)
        cookies_pop_up = self.driver.find_element(By.XPATH, "//button[text()='Only allow essential cookies']")
        cookies_pop_up.click()
        time.sleep(1)
        email_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_login.send_keys(EMAIL)
        password_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_login.send_keys(PASSWORD)
        time.sleep(2)
        password_login.send_keys(Keys.ENTER)
        time.sleep(13)
        turn_off_notifications = self.driver.find_element(By.XPATH, "//button[text()='Not Now']")
        turn_off_notifications.click()
        time.sleep(4)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/followers")
        time.sleep(7)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
        for button in all_buttons:
            # print(button.text)
            if button.text == "Follow":
                self.driver.execute_script("arguments[0].click();", button)
                time.sleep(2)
                
bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
