from __future__ import annotations
import pytest
import allure

from api.user_steps import UserSteps
from data.test_data import generate_api_user_data, generate_user_data
from models.user import User
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from utils.constants import BASE_URL, LOGIN_PAGE_URL
from utils.driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome|firefox")

@pytest.fixture
def browser(request) -> str:
    return request.config.getoption("--browser")

@pytest.fixture
def driver(browser):
    driver = create_driver(browser)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def api_user():

    steps = UserSteps()
    name, email, password = generate_api_user_data()
    user = User(email=email, password=password, name=name)

    with allure.step("Создание пользователя через API"):
        response = steps.create_user(user)
        assert response.status_code == 200, f"API register failed: {response.status_code} {response.text}"
        user.access_token = steps.extract_access_token(response)

    yield user

    with allure.step("Удаление пользователя через API"):
        delete_response = steps.delete_user(user)
        assert delete_response.status_code in (200, 202), f"API delete failed: {delete_response.status_code} {delete_response.text}"

@pytest.fixture
def register_ui_data():
    name, email, correct_password, wrong_password = generate_user_data()
    return {
        "name": name,
        "email": email,
        "correct_password": correct_password,
        "wrong_password": wrong_password,
    }

@pytest.fixture
def cleanup_user_by_api(request, register_ui_data):
    steps = UserSteps()
    user = User(
        email=register_ui_data["email"],
        password=register_ui_data["correct_password"],
        name=register_ui_data["name"],
    )

    def fin():
        if user.access_token:
            steps.delete_user(user)

    request.addfinalizer(fin)
    return user


@pytest.fixture
def logged_in_driver(driver, api_user):
    constructor = ConstructorPage(driver)

    with allure.step("Открытие формы логина кнопкой «Войти в аккаунт»"):
        constructor.wait_for_enter_account_button()
        constructor.click_enter_account_button()

    login_page = LoginPage(driver)
    with allure.step("Выполнить логин"):
        login_page.enter_credentials(api_user.email, api_user.password)
        login_page.click_enter_button()

    with allure.step("Дождаться кнопки «Оформить заказ» на главной"):
        constructor.wait_checkout_button()

    return driver
