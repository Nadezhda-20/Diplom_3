from selenium.webdriver.common.by import By

class RegisterPageLocators:
    HEADING = (By.XPATH, ".//*[normalize-space(text())='Регистрация']")
    
    NAME_FIELD = (By.XPATH, ".//label[normalize-space(text())='Имя']/../input")
    EMAIL_FIELD = (By.XPATH, ".//label[normalize-space(text())='Email']/../input")
    PASSWORD_FIELD = (By.XPATH, ".//label[normalize-space(text())='Пароль']/../input")
    REGISTER_BUTTON = (By.XPATH, ".//button[normalize-space(text())='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, ".//label[normalize-space(text())='Пароль']/ancestor::fieldset//p")
    ALREADY_REGISTERED_LINK = (By.XPATH, ".//*[contains(text(),'Уже зарегистрированы')]/a")
