from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Заголовок формы Для кого самокат
    form_order = [By.XPATH, './/div[contains(@class, "Order_Header__BZXOb") and contains(text(), "Для кого самокат")]']

    # Поле ввода: Имя
    input_name_form_order = [By.XPATH, './/div/input[contains(@placeholder, "* Имя")]']

    # Поле ввода: Фамилия
    input_surname_form_order = [By.XPATH, './/div/input[contains(@placeholder, "* Фамилия")]']

    # Поле ввода: Адрес: куда привезти заказ
    input_adress_form_order = [By.XPATH, './/div/input[contains(@placeholder, "* Адрес: куда привезти заказ")]']

    # Поле ввода: Телефон: на него позвонит курьер
    input_phone_form_order = [By.XPATH, './/div/input[contains(@placeholder, "* Телефон: на него позвонит курьер")]']

    # Кнопка Далее
    button_next_form_order = [By.XPATH, './/button[contains(text(), "Далее")]']

    # Поле ввода: Станция метро
    input_metro_form_order = [By.XPATH, './/div/input[contains(@placeholder, "* Станция метро")]']

    # Элемент в списке Станция метро
    element_in_metro_list_form_order = [By.XPATH, './/ul[contains(@class, "select-search__options")]/li[@data-index={}]/button']

    # Заголовок формы Про аренду
    form_arenda = [By.XPATH, './/div[contains(@class, "Order_Header__BZXOb") and contains(text(), "Про аренду")]']

    # Поле ввода: Когда привезти самокат
    input_date_dostavki_samokata = [By.XPATH, './/div/input[contains(@placeholder, "* Когда привезти самокат")]']

    # Поле ввода: Срок аренды
    period_picker_list = [By.XPATH, './/div[contains(@class, "Dropdown-placeholder") and contains(text(), "* Срок аренды")]/parent::div']

    # Выбор элемента в сроке аренды
    period_picker_list_elements = [By.XPATH, './/div[contains(@class, "Dropdown-menu")]/div']

    # Поле ввода: Цвет самоката
    color_picker_black = [By.XPATH, './/label[contains(@for, "black")]']
    color_picker_grey = [By.XPATH, './/label[contains(@for, "grey")]']

    # Поле ввода: Комментарий для курьера
    input_comment_for_courier = [By.XPATH, './/div/input[contains(@placeholder, "Комментарий для курьера")]']

    # Кнопка Заказать в форме Про аренду
    button_order_final = [By.XPATH, './/button[contains(@class, "Button_Middle__1CSJM") and contains(text(), "Заказать")]']

    # Тело страницы
    body_order_page = [By.XPATH, './/body']

    # Кнопка Да
    button_da_confirm_order = [By.XPATH, './/button[contains(text(), "Да")]']

    # Текст Заказ оформлен после успешного создания заказа
    text_order_completed = [By.XPATH, './/div[contains(@class, "Order_ModalHeader__3FDaJ")]']

