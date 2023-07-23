import pytest
import allure
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat

class TestOrder:

    @pytest.mark.allure
    @allure.title('Проверка успешного оформления заказа {name} {surname}')
    @allure.description('Нажимаем на кнопку Заказать, вводим данные клиента и параметры заказа, подтверждаем заказ и проверяем, что он оформлен')
    @pytest.mark.parametrize('order_button, name, surname, adress, metro, phone, date, period, color, comment',
        [
            ['header', 'Григорий', 'Лепс', 'Москва, ул. Иванова, 17-17', 3, '+70123456789', '13.09.2023', 1, 2, 'Очень прошу вас побыстрее'],
            ['middle', 'Алексей', 'Филиппов', 'Ярославль, ул. Иванова, 17-17', 5, '80123456789', '30.08.2023', 2, 1, 'Доставить до 15:00']
        ]
    )
    def test_order_from_head(self, my_firefox, order_button, name, surname, adress, metro, phone, date, period, color, comment):
        my_firefox.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPageSamokat(my_firefox)
        main_page.start_order(order_button)
        order_page = OrderPageSamokat(my_firefox)
        order_page.wait_form_order_visible()
        order_page.fill_client_form([name, surname, adress, metro, phone])
        order_page.fill_dostavka_form([date, period, color, comment])
        order_page.confirm_order()
        assert 'Заказ оформлен' in order_page.check_order()


