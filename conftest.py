import pytest
import allure

from pages.base_page import BasePage
from data import Urls
from api_client import User, Order
from driver_factory import create_driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on (chrome/firefox)",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode",
    )

def _create_driver(browser: str, headless: bool):
    browser = (browser or "chrome").strip().lower()
    if not headless:
        return create_driver(browser)

    if browser == "chrome":
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions

        options = ChromeOptions()
        options.add_argument("--remote-allow-origins=*")

        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options as FirefoxOptions

        options = FirefoxOptions()
        options.add_argument("--headless")
        return webdriver.Firefox(options=options)

    raise ValueError(f"Unsupported browser: {browser}. Supported: chrome, firefox")

@allure.step("Создание драйвера.")
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    drv = _create_driver(browser, headless)
    base = BasePage(drv)

    if headless:
        base.set_window_size(1920, 1080)
    else:
        base.maximize_window()

    base.change_url(Urls.URL_SERVICE)
    yield drv
    base.quit()

@allure.step("Создание тестового юзера")
@pytest.fixture
def user():
    u = User.register()
    yield u
    User.delete(u.get("accessToken"))

@allure.step("Создание заказа.")
@pytest.fixture
def submit_order(user):
    Order.submit_order(user)

@allure.step("Добавление токенов авторизации в LocalStorage и очистка данных после теста")
@pytest.fixture
def upload_tokens_to_session(driver, user):
    base = BasePage(driver)

    base.set_local_storage_item("accessToken", user["accessToken"])
    base.set_local_storage_item("refreshToken", user["refreshToken"])
    base.refresh_page()

    yield

    base.clear_local_storage()
    base.delete_all_cookies()
