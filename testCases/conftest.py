# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture()
# def setup():
#     driver =webdriver.Chrome(ChromeDriverManager().install())
#     return driver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture()
# def setup():
#     # Correctly set up Chrome options
#     chrome_options = webdriver.ChromeOptions()
#
#     # Use ChromeDriverManager properly
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#
#     yield driver  # Return the driver to the test function
#     driver.quit()  # Close the browser after test execution

import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


