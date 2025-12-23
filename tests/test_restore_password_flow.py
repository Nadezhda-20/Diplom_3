from pages.login_page import LoginPage
from pages.restore_password_page import RestorePasswordPage
from data import User
import allure

class TestRestorePassword:

    @allure.title('Успешный переход на страницу Восстановления пароля по кнопке «Восстановить пароль» на на странице Авторизации.')
    @allure.step("Шаги теста")
    def test_restore_password_on_click_restore_password_link_forgot_password_page_opens(self, driver):
        login_page = LoginPage(driver)
        login_page.transfer_to_login_page()
        login_page.restore_password_link_click()
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.check_forgot_password_page_transfer()

    @allure.title('Успешный переход на страницу Сброс пароля после ввода почты и клика по кнопке «Восстановить» на странице Восстановления пароля.')
    @allure.step("Шаги теста")
    def test_restore_password_on_click_restore_password_button_and_email_input_restore_password_page_opens(self, driver):
        login_page = LoginPage(driver)
        login_page.transfer_to_login_page()
        login_page.restore_password_link_click()
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.email_field_fill(User.email)
        restore_password_page.restore_password_button_click()
        restore_password_page.check_reset_password_page_transfer()

    @allure.title('Активация поля Пароль при клике по кнопке Показать/скрыть пароль.')
    @allure.step("Шаги теста")
    def test_restore_password_on_click_show_password_button_password_input_field_activates(self, driver):
        login_page = LoginPage(driver)
        login_page.transfer_to_login_page()
        login_page.restore_password_link_click()
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.email_field_fill(User.email)
        restore_password_page.restore_password_button_click()
        restore_password_page.show_password_button_click()
        restore_password_page.check_password_field_is_active()
