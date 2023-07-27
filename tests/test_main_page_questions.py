import allure
from pages.main_page import MainPageSamokat
from data import check_accordion_text

class TestQuestions:

    @allure.title('Проверка раскрытия пунктов с Вопросами о важном')
    @allure.description('Нажимаем на каждый элемент аккордиона и проверяем, что отобразилось соответствующее описание')
    def test_accordion_elements(self, my_firefox):
        main_page = MainPageSamokat(my_firefox)
        for i in range(8):
            main_page.wait_for_question_accordion_section_clickable(i)
            main_page.click_question_accordion_section(i)
            expected_text = check_accordion_text(i)
            actual_text = main_page.check_answer_text_accordion_section(i)
            assert (main_page.check_question_accordion_section_visible(i), actual_text) == ('true', expected_text)
