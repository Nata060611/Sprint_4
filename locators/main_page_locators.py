from selenium.webdriver.common.by import By

class MainPageLocators:

    # Отдельный вопрос в списке Вопросы о важном
    questions_accordion_section = [By.ID, 'accordion__heading-{}']

    # Кнопка Заказать в header
    button_order_header = [By.XPATH, './/button[not(contains(@class, "Button_Middle__1CSJM")) and contains(text(), "Заказать")]']

    # Кнопка Заказать в теле страницы
    button_order_middle = [By.XPATH, './/button[contains(@class, "Button_Middle__1CSJM") and contains(text(), "Заказать")]']