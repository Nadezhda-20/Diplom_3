from __future__ import annotations
import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_load()

    @allure.step("Ожидание загрузки страницы «Вход»")
    def wait_for_page_load(self) -> None:
        self.wait_visible(LoginPageLocators.HEADING, timeout=15)

    @allure.step("Ввод данных пользователя: email {email} и пароль {password}")
    def enter_credentials(self, email: str, password: str) -> None:
        self.type(LoginPageLocators.EMAIL_FIELD, email)
        self.type(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Нажатие на кнопку «Войти»")
    def click_enter_button(self) -> None:
        self.click(LoginPageLocators.ENTER_BUTTON)

    @allure.step("Переход по ссылке «Зарегистрироваться»")
    def click_registration_link(self) -> None:
        self.click(LoginPageLocators.REGISTRATION_LINK)

    @allure.step("Переход по ссылке «Восстановить пароль»")
    def click_recover_password_link(self) -> None:
        self.click(LoginPageLocators.RECOVER_PASSWORD_LINK)
