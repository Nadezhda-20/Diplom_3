from selenium.webdriver.common.by import By

class HeaderPageLocators:

    # Кнопка "Личный кабинет"
    user_account_link = [By.XPATH, ".//a[contains(@class,'AppHeader_header__link') and @href='/account']"]
    # Кнопка "Конструктор"
    constructor = [By.XPATH, ".//a[contains(@class,'AppHeader_header__link') and @href='/']"]
    # Кнопка "Лента заказов"
    orders_line = [By.XPATH, ".//a[contains(@class,'AppHeader_header__link') and @href='/feed']"]
