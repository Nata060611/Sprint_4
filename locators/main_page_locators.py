from selenium.webdriver.common.by import By

class MainPageLocators:

    # Отдельный вопрос в списке Вопросы о важном
    questions_accordion_section = [By.ID, 'accordion__heading-{}']

    # Отдельный ответ в списке Вопросы о важном
    questions_accordion_section_answer = [By.XPATH, './/div[@id="accordion__heading-{}"]']

    # Кнопка Заказать в header
    button_order_header = [By.XPATH, '(.//button[contains(text(), "Заказать")])[1]']

    # Кнопка Заказать в теле страницы
    button_order_middle = [By.XPATH, '(.//button[contains(text(), "Заказать")])[2]']

    # Логотип Яндекс
    yandex_logo = [By.XPATH, './/a[contains(@class, "Header_LogoYandex__3TSOI")]']
