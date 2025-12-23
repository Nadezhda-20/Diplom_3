from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure
from data import Urls

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание появления заголовка Вход')
    def login_header_wait(self):
       self.wait_visibility_of_element(LoginPageLocators.login_header)

    @allure.step('Переход на страницу Авторизации')
    def transfer_to_login_page(self):
        self.change_url(Urls.LOGIN)
        self.login_header_wait()

    @allure.step('Ожидание кликабельности кнопки Восстановить пароль')
    def restore_password_link_wait(self):
        self.wait_clickability_of_element(LoginPageLocators.restore_password_link)

    @allure.step('Клик по кнопке Восстановить пароль')
    def restore_password_link_click(self):
        self.restore_password_link_wait()
        self.click_on_element(LoginPageLocators.restore_password_link)

    @allure.step('Проверка перехода на страницу Авторизации')
    def check_login_page_transfer(self):
        self.login_header_wait()
        current_url = self.get_current_url()
        assert current_url == Urls.LOGIN, f'Смена страницы не произошла: {current_url}'
