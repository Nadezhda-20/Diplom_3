import allure

from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from utils.constants import LOGIN_PAGE_URL, REGISTER_PAGE_URL


@allure.epic("Stellar Burgers UI")
@allure.feature("Регистрация")
class TestRegister:
    @allure.title("Позитивный тест на успешную регистрацию пользователя")
    @allure.description("Позитивный тест на создание пользователя с заполненными полями (UI), логин и проверка данных профиля")
    def test_successful_registration(self, driver, register_ui_data, cleanup_user_by_api):
        constructor = ConstructorPage(driver)

        with allure.step("Открыть личный кабинет для перехода к логину"):
            constructor.wait_for_personal_account_button()
            constructor.click_personal_account_button()

        login_page = LoginPage(driver)

        with allure.step("Перейти на регистрацию"):
            login_page.click_registration_link()

        register_page = RegisterPage(driver)
        register_page.wait_for_page_load()

        with allure.step("Заполнить форму регистрации"):
            register_page.fill_in_registration_form(
                register_ui_data["name"],
                register_ui_data["email"],
                register_ui_data["correct_password"],
            )

        with allure.step("Убедиться, что открылась страница логина"):
            login_page = LoginPage(driver)
            assert login_page.current_url() == LOGIN_PAGE_URL, "После регистрации не открылась страница логина"

        with allure.step("Войти под созданным пользователем"):
            login_page.enter_credentials(register_ui_data["email"], register_ui_data["correct_password"])
            login_page.click_enter_button()

        with allure.step("Дождаться загрузки главной страницы после логина"):
            constructor.wait_checkout_button()

        with allure.step("Открыть личный кабинет"):
            constructor.click_personal_account_button()

        profile = MainPage(driver)

        with allure.step("Дождаться загрузки страницы профиля"):
            profile.wait_profile_page_load()

        with allure.step("Проверить имя и email в профиле"):
            assert profile.get_name_value() == register_ui_data["name"], "Имя в профиле не совпадает"
            assert profile.get_email_value().lower() == register_ui_data["email"].lower(), "Email в профиле не совпадает"

    @allure.title("Проверка на невозможность создание пользователя с некорректным паролем")
    @allure.description("Негативный тест на невозможность создания пользователя с 5-значным паролем")
    def test_error_password(self, driver, register_ui_data):
        constructor = ConstructorPage(driver)

        with allure.step("Открыть личный кабинет для перехода к логину"):
            constructor.wait_for_personal_account_button()
            constructor.click_personal_account_button()

        login_page = LoginPage(driver)

        with allure.step("Перейти на регистрацию"):
            login_page.click_registration_link()

        register_page = RegisterPage(driver)
        register_page.wait_for_page_load()

        with allure.step("Заполнить форму регистрации некорректным паролем"):
            register_page.fill_in_registration_form(
                register_ui_data["name"],
                register_ui_data["email"],
                register_ui_data["wrong_password"],
            )

        assert register_page.password_error_text() == "Некорректный пароль", "Текст ошибки под полем «Пароль» отличается"
        assert register_page.current_url() == REGISTER_PAGE_URL, "Ожидалось остаться на странице регистрации"
