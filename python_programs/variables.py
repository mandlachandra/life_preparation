# from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# try:
#     element = driver.find_element(By.ID,"login")
#     element.click()
#
# except NoSuchElementException:
#     print("login button not found")


#how to handle multiple exceptions

# from selenium.common.exceptions import (
#     NoSuchElementException,
#     ElementNotInteractableException,
#     TimeoutException
# )
# try:
#     driver.find_element(By.ID,"submit").click()
#
# except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as e:
#     print(f"Error occured: {type(e).__name__}")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Alerts.html")
# driver.maximize_window()
# time.sleep(2)
#
# element = driver.find_element(By.XPATH,'//button[contains(@class,"btn btn-danger")]').click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print("Alert text is:",alert.text)
# alert.accept()
# driver.quit()



# element =driver.find_element(By.XPATH,"(//button[contains(text(),'click')])[1]")
# element.click()
# time.sleep(2)
#
# main_window = driver.current_window_handle
# print(main_window)
#
# for handle in driver.window_handles:
#     if handle!=main_window:
#         driver.switch_to.window(handle)
#         print("title of new tab:",driver.title)
#         driver.close()
#
# driver.switch_to.window(main_window)
# print("back to main window:",driver.title)
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

#Alert Code

# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Alerts.html")
# time.sleep(2)
#
# element = driver.find_element(By.XPATH,'//button[contains(@class,"btn btn-danger")]').click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print("alert text is:",alert.text)
# alert.accept()
# driver.quit()

#Frames
# driver = webdriver.Chrome()
# driver.get('https://demo.automationtesting.in/Frames.html')
# driver.maximize_window()
# time.sleep(2)
#
# driver.switch_to.frame("frame1")
# heading = driver.find_element(By.XPATH,'(//div[contains(@class,"col-xs-6 col-xs-offset-5")]//child::input)[1]')
# print("frame text:",heading.text)
# driver.switch_to.default_content()
# driver.quit()

#Window Handles
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/browser-windows")
# driver.maximize_window()
# time.sleep(2)
#
# parent_handle = driver.current_window_handle
# print("parent handle:",parent_handle)
#
# driver.find_element(By.XPATH,"//button[@id='tabButton']").click()
# time.sleep(2)
#
# #get all windows
# handles = driver.window_handles
# print("All handles:",handles)
#
# #switch to the child window(2nd handle)
# for handle in handles:
#     if handle!=parent_handle:
#         driver.switch_to.window(handle)
#         print("child window Title:",driver.title)
#         time.sleep(2)
#         driver.close()
#
# #switch back to parent window
# driver.switch_to.window(parent_handle)
# print("Back to Parent Title:",driver.title)
#
# driver.quit()
#Window Handles
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/browser-windows")
# driver.maximize_window()
# time.sleep(2)
# parent_handle = driver.current_window_handle
# print("parent handle:",parent_handle)
# driver.find_element(By.XPATH,"//button[@id='tabButton']").click()
# time.sleep(2)
# handles = driver.window_handles
# print("All handles",handles)
#
# for handle in handles:
#     if handle!=parent_handle:
#         driver.switch_to.window(handle)
#         print("child window:",driver.title)
#         driver.close()
#
# driver.switch_to.window(parent_handle)
# print("Back to parent title:",driver.title)

#......................
#Dropdown
# from selenium import webdriver
# #from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()
# driver.get("")
# driver.maximize_window()
# time.sleep(2)
#
# dropdown = driver.find_elements(By.ID,"cityDropdown")
#
# all_options = dropdown.options
#
# cities = [option.text for option in all_options]
# print("cities in dropdown:",cities)
# driver.quit()

#..................
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#Mouse Hover
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/menu")
# driver.maximize_window()
# time.sleep(4)
# #locate the element to hover
# menu = driver.find_element(By.XPATH,'//a[text()="Main Item 2"]')
#
# #create actionchains object
# actions = ActionChains(driver)
# actions.move_to_element(menu).perform()
# time.sleep(2)
#
# #locate a submenu item revealed after hover
# submenu = driver.find_element(By.XPATH,"//a[text()='SUB SUB LIST »']")
# actions.move_to_element(submenu).perform()
#
# #click on a sub sub menu item
# sub_sub_item = driver.find_element(By.XPATH,"//a[text()='Sub Sub Item 1']")
# sub_sub_item.click()
#
# time.sleep(2)
# driver.quit()







