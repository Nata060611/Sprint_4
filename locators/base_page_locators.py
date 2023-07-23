from selenium.webdriver.common.by import By

class BasePageLocators:

    # Логотип сервиса Самокат
    samokat_logo = [By.XPATH, './/a[contains(@class, "Header_LogoScooter__3lsAR")]']

    # Логотип Яндекс
    yandex_logo = [By.XPATH, './/a[contains(@class, "Header_LogoYandex__3TSOI")]']
