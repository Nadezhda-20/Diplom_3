from selenium.webdriver.common.by import By

class RegisterPageLocators:
    HEADING = (By.XPATH, ".//*[text()='Регистрация']")

    NAME_FIELD = (By.XPATH, ".//fieldset[1]//input")
    EMAIL_FIELD = (By.XPATH, ".//fieldset[2]//input")
    PASSWORD_FIELD = (By.XPATH, ".//fieldset[3]//input")

    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, ".//fieldset[3]//p")
    ALREADY_REGISTERED_LINK = (By.XPATH, ".//*[text()='Уже зарегистрированы?']/a")
