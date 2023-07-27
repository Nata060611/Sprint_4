from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element_direct(self, locator):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*locator))

    def wait_for_clickable_and_scroll(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    def set_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text
