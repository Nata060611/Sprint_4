from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPageSamokat(BasePage):

    loc = MainPageLocators()

    @allure.step('Кликаем на элемент аккордиона номер {number}')
    def click_question_accordion_section(self, number):
        method, locator = self.loc.questions_accordion_section
        new_locator = method, locator.format(number)
        self.click_on_element_direct(new_locator)

    @allure.step('Проверяем значение "aria-expanded" у элемента номер {number}')
    def check_question_accordion_section_visible(self, number):
        method, locator = self.loc.questions_accordion_section
        new_locator = method, locator.format(number)
        return self.driver.find_element(*new_locator).get_attribute('aria-expanded')

    @allure.step('Проверяем текст у элемента аккордиона номер {number}')
    def check_answer_text_accordion_section(self, number):
        method, locator = self.loc.questions_accordion_section_answer
        new_locator = method, locator.format(number) + '/parent::div/parent::div/div[2]/p'
        return_text = self.driver.find_element(*new_locator).get_attribute("textContent")
        return return_text

    @allure.step('Ждем, когда элемент аккордиона {number} можно кликнуть')
    def wait_for_question_accordion_section_clickable(self, number):
        method, locator = self.loc.questions_accordion_section
        new_locator = method, locator.format(number)
        self.wait_for_clickable_and_scroll(new_locator)

    @allure.step('Кликаем на кнопку Заказать в {button} на главной странице')
    def start_order(self, button):
        if button == 'header':
            self.wait_for_clickable_and_scroll(self.loc.button_order_header)
            self.click_on_element_direct(self.loc.button_order_header)
        else:
            self.wait_for_clickable_and_scroll(self.loc.button_order_middle)
            self.click_on_element_direct(self.loc.button_order_middle)

    @allure.step('Получаем текст 2го элемента в Вопросах о важном')
    def check_mainpage(self):
        method, locator = self.loc.questions_accordion_section
        new_locator = method, locator.format(1)
        self.wait_for_clickable_and_scroll(new_locator)
        return self.get_element_text(new_locator)

    @allure.step('Кликаем на логотип Яндекс на главной странице')
    def click_logo_yandex(self):
        self.wait_for_clickable_and_scroll(self.loc.yandex_logo)
        self.click_on_element(self.loc.yandex_logo)