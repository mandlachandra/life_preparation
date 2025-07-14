import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage

class Test_001_Login:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "//input[@name= 'username']"
    password = "//input[@name= 'password']"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title =="Orange HRM":

            assert True
        else:
            assert False

    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.Login_button()
        act_title = self.driver.title
        if act_title=="Orange HRM":
            assert True
        else:
            assert False

