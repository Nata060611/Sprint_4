import pytest
from selenium import webdriver

@pytest.fixture
def my_firefox():
    my_browser = webdriver.Firefox()
    yield my_browser
    my_browser.quit()
