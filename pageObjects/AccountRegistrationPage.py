# from selenium.webdriver.common.by import By
#
# class AccountRegistrationPage():
#
#     txt_firstname_name = "firstname"
#     txt_lastname_name = "lastname"
#     txt_email_name = "email"
#     txt_telphone_name = "telephone"
#     txt_password_name = "password"
#     txt_confpassword_name = "confirm"
#     chk_policy_name = "agree"
#     btn_cont_xpath = "//input[@value='continue']"
#     txt_msg_conf_xpath = "//h1[normalize-space()='your Account has been created!']"
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     def setFirstname(self,fname):
#         self.driver.find_element(By.NAME, self.txt_firstname_name).sendkeys(fname)
#
#     def setLastName(self,lname):
#         self.driver.find_element(By.NAME, self.txt_lastname_name).sendkeys(lname)
#
#     def setEmail(self, driver):
#         self.driver.find_element(By.NAME,self.txt_email_name).sendkeys("email")
#
#     def setTelephone(self,tel):
#         self.driver.find_element(By.NAME,self.txt_telphone_name).sendkeys(tel)
#
#     def setPassword(self, driver):
#         self.driver.find_element(By.NAME,self.txt_password_name).sendkeys("pwd")
#
#     def setConfirmPassword(self, driver):
#         self.driver.find_element(By.NAME, self.txt_confpassword_name).sendkeys("cnfpwd")
#
#     def setPrivacyPoliy(self, driver):
#         self.driver.find_element(By.NAME, self.chk_policy_name).click()
#
#     def clickContinue(self,driver):
#         self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()
#
#     def getconfirmationmsg(self,driver):
#         try:
#             return self.driver.find_element(By.XPATH, self.txt_msg_conf_xpath).text
#
#         except:
#             None


