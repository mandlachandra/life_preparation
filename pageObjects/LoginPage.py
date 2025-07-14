from selenium.webdriver.common.by import By
from selenium import webdriver

class Loginpage():

    textbox_username_xpath ="//input[@name= 'username']"
    textbox_password_xpath = "//input[@name= 'password']"
    Login_button = "//button[@type='submit']"

    driver = webdriver.Chrome()

    def __init__(self):
        self.driver = driver

    def setUserName(self):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickButton(self):
        self.driver.find_element(By.XPATH,self.Login_button).click()