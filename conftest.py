from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(r"drivers/chromedriver_win32/chromedriver.exe")
    return  driver