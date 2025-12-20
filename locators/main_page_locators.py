from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_TEXT = (By.XPATH, ".//*[contains(text(), 'изменить свои персональные данные')]")
    
    NAME_FIELD = (
        By.XPATH,
        ".//label[normalize-space(.)='Имя']"
        "/ancestor::div[contains(@class,'input')]//input"
        " | .//input[@name='name']",
    )
 
    EMAIL_FIELD = (
        By.XPATH,
        ".//label[normalize-space(.)='Логин' or normalize-space(.)='Email' or normalize-space(.)='E-mail']"
        "/ancestor::div[contains(@class,'input')]//input"
        " | .//input[@name='login' or @name='email']",
    )
