from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPageSamokat(BasePage):

    loc = OrderPageLocators()

    @allure.step('Ожидаем отображения формы заказа')
    def wait_form_order_visible(self):
        self.wait_for_clickable_and_scroll(self.loc.form_order)

    @allure.step('Заполняем данные клиента')
    def fill_client_form(self, client):
        self.set_text(self.loc.input_name_form_order, client[0])
        self.set_text(self.loc.input_surname_form_order, client[1])
        self.set_text(self.loc.input_adress_form_order, client[2])
        self.set_text(self.loc.input_phone_form_order, client[4])
        self.click_on_element(self.loc.input_metro_form_order)
        method, locator = self.loc.element_in_metro_list_form_order
        new_locator = method, locator.format(client[3])
        self.wait_for_clickable_and_scroll(new_locator)
        self.click_on_element(new_locator)
        self.click_on_element_direct(self.loc.button_next_form_order)

    @allure.step('Заполняем данные доставки')
    def fill_dostavka_form(self, delivery):
        self.wait_for_clickable_and_scroll(self.loc.input_date_dostavki_samokata)
        self.set_text(self.loc.input_date_dostavki_samokata, delivery[0])
        self.click_on_element(self.loc.body_order_page)
        self.click_on_element(self.loc.period_picker_list)
        method, locator = self.loc.period_picker_list_elements
        new_locator = method, locator + '[' + str(delivery[1]) + ']'
        self.wait_for_clickable_and_scroll(new_locator)
        self.click_on_element(new_locator)
        if delivery[2] == 1:
            self.click_on_element(self.loc.color_picker_black)
        else:
            self.click_on_element(self.loc.color_picker_grey)
        self.set_text(self.loc.input_comment_for_courier, delivery[3])
        self.click_on_element_direct(self.loc.button_order_final)

    @allure.step('Нажимаем на кнопку подтверждения заказа')
    def confirm_order(self):
        self.wait_for_clickable_and_scroll(self.loc.button_da_confirm_order)
        self.click_on_element_direct(self.loc.button_da_confirm_order)

    @allure.step('Получаем текст со статусом заказа')
    def check_order(self):
        self.wait_for_clickable_and_scroll(self.loc.text_order_completed)
        return self.get_element_text(self.loc.text_order_completed)

    @allure.step('Кликаем на логотип Самокат на странице заказа')
    def click_logo_samokat(self):
        self.wait_for_clickable_and_scroll(self.base_loc.samokat_logo)
        self.click_on_element(self.base_loc.samokat_logo)