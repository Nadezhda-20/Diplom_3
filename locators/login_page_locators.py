from selenium.webdriver.common.by import By

class LoginPageLocators:

    # Гиперссылка "Восстановить пароль"
    restore_password_link = [By.XPATH, ".//a[text()='Восстановить пароль']"]
    # Заголовок Вход
    login_header = [By.XPATH, ".//h2[text()='Вход']"]
