import pytest
from selenium import webdriver

@pytest.fixture
def my_firefox():
    my_browser = webdriver.Firefox()
    my_browser.get('https://qa-scooter.praktikum-services.ru')
    yield my_browser
    my_browser.quit()
