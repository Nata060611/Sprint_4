import pytest
import allure
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat
from data import get_client

class TestOrder:

    @allure.title('Проверка успешного оформления заказа по кнопке в {order_button}')
    @allure.description('Нажимаем на кнопку Заказать, вводим данные клиента и параметры заказа, подтверждаем заказ и проверяем, что он оформлен')
    @pytest.mark.parametrize('order_button, client',
        [
            ['header', get_client(1)],
            ['middle', get_client(2)]
        ]
    )
    def test_order(self, my_firefox, order_button, client):
        main_page = MainPageSamokat(my_firefox)
        main_page.start_order(order_button)
        order_page = OrderPageSamokat(my_firefox)
        order_page.wait_form_order_visible()
        order_page.fill_client_form([client['name'], client['surname'], client['address'], client['metro'], client['phone']])
        order_page.fill_dostavka_form([client['date'], client['period'], client['color'], client['comment']])
        order_page.confirm_order()
        assert 'Заказ оформлен' in order_page.check_order()


