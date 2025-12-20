from __future__ import annotations
import allure
from locators.register_page_locators import RegisterPageLocators
from pages.base_page import BasePage

class RegisterPage(BasePage):
    @allure.step("Ожидание загрузки страницы «Регистрация»")
    def wait_for_page_load(self) -> None:
        self.wait_visible(RegisterPageLocators.HEADING, timeout=15)

    @allure.step("Заполнение формы регистрации: имя {name}, email {email}, пароль {password}")
    def fill_in_registration_form(self, name: str, email: str, password: str) -> None:
        self.type(RegisterPageLocators.NAME_FIELD, name)
        self.type(RegisterPageLocators.EMAIL_FIELD, email)
        self.type(RegisterPageLocators.PASSWORD_FIELD, password)
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("Получение текста ошибки под полем «Пароль»")
    def password_error_text(self) -> str:
        return self.get_text(RegisterPageLocators.PASSWORD_ERROR)

    @allure.step("Нажатие на ссылку «Уже зарегистрированы? Войти»")
    def click_already_registered_link(self) -> None:
        self.click(RegisterPageLocators.ALREADY_REGISTERED_LINK)
