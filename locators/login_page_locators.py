from selenium.webdriver.common.by import By


class LoginPageLocators:
    HEADING = (By.XPATH, "//*[contains(text(), 'Вход')]")

    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/../input")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/../input")

    ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    REGISTRATION_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")
    RECOVER_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
