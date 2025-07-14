import os.path
import time

from pageObjects.LoginPage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.customLogger import LogGen


class Test_001_AccountReg:
    baseURL = "https://demoqa.com/browser-windows"
    time.sleep(2)
    logger = LogGen.loggen()

    # def test_account_reg(self,setup):
    #     self.logger.info("**** test_001 has started....")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #
    #     self.hp = HomePage(self.driver)
    #     self.hp.clickMyAccount()
    #     self.hp.clickRegister()
    #     self.regpage = AccountRegistrationPage(self.driver)
    #
    #     self.regpage.setFirstname("John")
    #     self.regpage.setLastName("max")
    #     self.email = randomeString.random_string_generator()+'gmail.com'
    #     self.regpage.setEmail(self.email)
    #     self.regpage.setPassword("123")
    #     self.regpage.setConfirmPassword("123")
    #     self.regpage.setPrivacyPoliy()
    #     self.regpage.clickContinue()
    #     self.confmsg = self.regpage.getconfirmationmsg()
    #     self.driver.close()
    #     if self.confmsg == "Your Account has been created!":
    #         assert True
    #         self.driver.close()
    #
    #     else:
    #         self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
    #         self.driver.close()
    #
    #         assert False
