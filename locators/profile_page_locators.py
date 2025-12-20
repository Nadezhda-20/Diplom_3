from selenium.webdriver.common.by import By

class ProfilePageLocators:    
    HEADING = (By.XPATH, ".//*[text()='Восстановление пароля']")
    REMEMBERED_PASSWORD_LINK = (By.XPATH, ".//a[text()='Войти']")
