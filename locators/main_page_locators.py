from selenium.webdriver.common.by import By

class MainPageLocators:   
    PROFILE_TEXT = (By.XPATH, ".//*[contains(text(), 'изменить свои персональные данные')]")
    NAME_FIELD = (By.XPATH, ".//li[1]//input")
    EMAIL_FIELD = (By.XPATH, ".//li[2]//input")
