import pytest
import allure
from pages.order_page import OrderPageSamokat
from pages.main_page import MainPageSamokat
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogos:

    @allure.title('Проверка перехода по логотипу Самокат')
    @allure.description('Нажимаем на логотип Самокат на странице заказа и проверяем, что перешли на главную страницу')
    def test_logo_samokat_order_page(self, my_firefox):
        my_firefox.get('https://qa-scooter.praktikum-services.ru/order')
        order_page = OrderPageSamokat(my_firefox)
        order_page.click_logo_samokat()
        main_page = MainPageSamokat(my_firefox)
        assert 'Хочу сразу несколько самокатов' in main_page.check_mainpage()

    @allure.title('Проверка перехода по логотипу Яндекс')
    @allure.description('Нажимаем на логотип Яндекс на главной странице и проверяем, что в новой вкладке открылась страница yandex.ru')
    def test_logo_yandex_main_page(self, my_firefox):
        main_page = MainPageSamokat(my_firefox)
        main_page.click_logo_yandex()
        WebDriverWait(my_firefox, 10).until(expected_conditions.number_of_windows_to_be(2))
        my_firefox.switch_to.window(my_firefox.window_handles[1])
        WebDriverWait(my_firefox, 10).until(expected_conditions.url_contains('yandex.ru'))
        current_url = my_firefox.current_url
        expected_url = 'yandex.ru'
        assert expected_url in current_url, f"Ожидался URL: {expected_url}, получен URL: {current_url}"
