from pages.header_page import HeaderPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
import allure

class TestProfilePage:

    @allure.title('Переход авторизованного пользователя на страницу Личный кабинет по клику на кнопку «Личный кабинет» в шапке страницы')
    @allure.step("Шаги теста")
    def test_profile_page_user_authorized_on_click_profile_button_profile_page_opens(self, driver, upload_tokens_to_session):
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        profile_page = ProfilePage(driver)
        profile_page.check_profile_page_transfer()

    @allure.title('Переход неавторизованного пользователя на страницу Авторизации по клику на кнопку «Личный кабинет» в шапке страницы')
    @allure.step("Шаги теста")
    def test_profile_page_user_not_authorized_on_click_profile_button_login_page_opens(self, driver):
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        login_page = LoginPage(driver)
        login_page.check_login_page_transfer()

    @allure.title('Переход авторизованного пользователя в раздел История заказов по клику на кнопку «История заказов» в Личном кабинете')
    @allure.step("Шаги теста")
    def test_profile_page_on_click_history_tab_history_page_opens(self, driver, upload_tokens_to_session):
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        profile_page = ProfilePage(driver)
        profile_page.history_tab_click()
        profile_page.check_history_page_transfer()

    @allure.title('Выход авторизованного пользователя из системы и переход на страницу Авторизации по клику на кнопку «Выход» в Личном кабинете')
    @allure.step("Шаги теста")
    def test_profile_page_on_click_logout_button_login_page_opens(self, driver, upload_tokens_to_session):
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        profile_page = ProfilePage(driver)
        profile_page.logout_button_click()
        profile_page.check_login_page_transfer()
