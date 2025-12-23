from locators.restore_password_page_locators import RestorePasswordPageLocators
from pages.base_page import BasePage
import allure
from data import Urls

class RestorePasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки кнопки Восстановить')
    def restore_password_button_wait(self):
        self.wait_clickability_of_element(RestorePasswordPageLocators.restore_password_button)

    @allure.step('Проверка перехода на страницу Восстановление пароля')
    def check_forgot_password_page_transfer(self):
        self.restore_password_button_wait()
        current_url = self.get_current_url()
        assert current_url == Urls.FORGOT_PASSWORD, f'Смена страницы не произошла: {current_url}'

    @allure.step('Заполнение поля email')
    def email_field_fill(self, email):
        self.send_keys_to_input(RestorePasswordPageLocators.email_field, email)

    @allure.step('Клик по кнопке Восстановить')
    def restore_password_button_click(self):
        self.restore_password_button_wait()
        self.click_on_element(RestorePasswordPageLocators.restore_password_button)

    @allure.step('Ожидание загрузки кнопки Сохранить')
    def save_password_button_wait(self):
        self.wait_visibility_of_element(RestorePasswordPageLocators.save_password_button)

    @allure.step('Проверка перехода на страницу Сброс пароля')
    def check_reset_password_page_transfer(self):
        self.save_password_button_wait()
        current_url = self.get_current_url()
        assert current_url == Urls.RESET_PASSWORD, f'Смена страницы не произошла: {current_url}'

    @allure.step('Ожидание загрузки кнопки Показать/скрыть пароль')
    def show_password_button_wait(self):
        self.wait_clickability_of_element(RestorePasswordPageLocators.show_password_button)

    @allure.step('Клик по кнопке Показать/скрыть пароль в поле password')
    def show_password_button_click(self):
        self.show_password_button_wait()
        self.click_on_element(RestorePasswordPageLocators.show_password_button)

    @allure.step('Проверка активации поля Пароль')
    def check_password_field_is_active(self):
        div_status = self.get_element_class(RestorePasswordPageLocators.pass_input_div)
        label_status = self.get_element_class(RestorePasswordPageLocators.pass_input_label)
        assert 'input_status_active' in div_status and 'input__placeholder-focused' in label_status, 'Поле не сменило статус на активный.'
