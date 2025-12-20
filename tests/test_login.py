import allure
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.register_page import RegisterPage


@allure.epic("Stellar Burgers UI")
@allure.feature("Логин")
class TestLogin:
    @allure.title("Позитивный тест на вход по кнопке «Войти в аккаунт»")
    @allure.description("Создание пользователя через API, логин через кнопку «Войти в аккаунт», проверка email в профиле")
    def test_login_via_enter_account_button(self, driver, api_user):
        constructor = ConstructorPage(driver)

        with allure.step("Открыть форму логина"):
            constructor.wait_for_enter_account_button()
            constructor.click_enter_account_button()

        login_page = LoginPage(driver)
        with allure.step("Выполнить логин"):
            login_page.enter_credentials(api_user.email, api_user.password)
            login_page.click_enter_button()

        with allure.step("Открыть личный кабинет"):
            constructor.wait_checkout_button()
            constructor.click_personal_account_button()

        profile = MainPage(driver)
        profile.wait_profile_page_load()

        "Email в профиле не совпадает с зарегистрированным"
        assert profile.get_email_value().lower() == api_user.email.lower()

    @allure.title("Позитивный тест на вход по кнопке «Личный кабинет»")
    @allure.description("Создание пользователя через API, переход по «Личный кабинет», логин, проверка email в профиле.")
    def test_login_via_personal_account_button(self, driver, api_user):
        constructor = ConstructorPage(driver)

        with allure.step("Открыть форму логина через «Личный кабинет»"):
            constructor.wait_for_personal_account_button()
            constructor.click_personal_account_button()

        login_page = LoginPage(driver)
        with allure.step("Выполнить логин"):
            login_page.enter_credentials(api_user.email, api_user.password)
            login_page.click_enter_button()

        with allure.step("Открыть личный кабинет после логина"):
            constructor.wait_checkout_button()
            constructor.click_personal_account_button()

        profile = MainPage(driver)
        profile.wait_profile_page_load()

        assert profile.get_email_value().lower() == api_user.email.lower(), "Email в профиле не совпадает с зарегистрированным"


    @allure.title("Позитивный тест на вход по ссылке в форме регистрации")
    @allure.description("Создание пользователя через API, переход на регистрацию, затем «Уже зарегистрированы? Войти», логин, проверка email")
    def test_login_via_registration_form_link(self, driver, api_user):
        constructor = ConstructorPage(driver)

        with allure.step("Открыть форму логина"):
            constructor.wait_for_enter_account_button()
            constructor.click_enter_account_button()

        login_page = LoginPage(driver)
        with allure.step("Перейти на регистрацию и обратно по ссылке"):
            login_page.click_registration_link()
            register_page = RegisterPage(driver)
            register_page.wait_for_page_load()
            register_page.click_already_registered_link()

        login_page = LoginPage(driver)
        with allure.step("Выполнить логин"):
            login_page.enter_credentials(api_user.email, api_user.password)
            login_page.click_enter_button()

        with allure.step("Открыть личный кабинет после логина"):
            constructor.wait_checkout_button()
            constructor.click_personal_account_button()

        profile = MainPage(driver)
        profile.wait_profile_page_load()

        assert profile.get_email_value().lower() == api_user.email.lower(), "Email в профиле не совпадает с зарегистрированным"


    @allure.title("Позитивный тест на вход по ссылке в форме восстановления пароля")
    @allure.description("Создание пользователя через API, переход на восстановление, затем «Войти», логин, проверка email")
    def test_login_via_recover_password_form_link(self, driver, api_user):
        constructor = ConstructorPage(driver)

        with allure.step("Открыть форму логина"):
            constructor.wait_for_enter_account_button()
            constructor.click_enter_account_button()

        login_page = LoginPage(driver)
        with allure.step("Перейти на восстановление пароля и вернуться по ссылке «Войти»"):
            login_page.click_recover_password_link()
            recover = ProfilePage(driver)
            recover.wait_profile_page_load()
            recover.click_remembered_password()

        login_page = LoginPage(driver)
        with allure.step("Выполнить логин"):
            login_page.enter_credentials(api_user.email, api_user.password)
            login_page.click_enter_button()

        with allure.step("Открыть личный кабинет после логина"):
            constructor.wait_checkout_button()
            constructor.click_personal_account_button()

        profile = MainPage(driver)
        profile.wait_profile_page_load()

        assert profile.get_email_value().lower() == api_user.email.lower(), "Email в профиле не совпадает с зарегистрированным"

