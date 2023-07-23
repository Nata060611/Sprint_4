import pytest
import allure
from pages.main_page import MainPageSamokat

class TestQuestions:

    @pytest.mark.allure
    @allure.title('Проверка раскрытия пунктов с Вопросами о важном')
    @allure.description('Нажимаем на каждый элемент аккордиона и проверяем, что отобразилось соответствующее описание')
    def test_accordion_elements(self, my_firefox):
        my_firefox.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPageSamokat(my_firefox)
        for i in range(8):
            main_page.wait_for_question_accordion_section_clickable(i)
            main_page.click_question_accordion_section(i)
            assert main_page.check_question_accordion_section_visible(i) == 'true'
