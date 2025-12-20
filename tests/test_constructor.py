import allure
import pytest

from pages.constructor_page import ConstructorPage


@allure.epic("Stellar Burgers UI")
@allure.feature("Конструктор")
class TestConstructor:
    @allure.title("Проверка: переключение на раздел «Булки» с раздела «Соусы»")
    @allure.description(
        "При открытии главной страницы переключаемся на «Соусы» и обратно на «Булки». "
        "Проверяем, что активной становится вкладка «Булки»."
    )
    def test_buns_active_on_load(self, driver):
        constructor = ConstructorPage(driver)

        with allure.step("Перейти на вкладку «Соусы» и обратно на «Булки»"):
            constructor.wait_for_enter_account_button()
            constructor.click_sauces_tab()
            constructor.wait_for_sauces_active(15)
            constructor.click_buns_tab()
            constructor.wait_for_buns_active(15)

        assert constructor.is_buns_tab_active(), "Вкладка «Булки» не стала активной"

    @pytest.mark.parametrize(
        "tab_name, click_tab, wait_active, is_active",
        [
            ("Соусы", ConstructorPage.click_sauces_tab, ConstructorPage.wait_for_sauces_active, ConstructorPage.is_sauces_tab_active),
            ("Начинки", ConstructorPage.click_fillings_tab, ConstructorPage.wait_for_fillings_active, ConstructorPage.is_fillings_tab_active),
        ],
        ids=["switch_to_sauces", "switch_to_fillings"],
    )
    @allure.title("Переключение вкладок конструктора")
    @allure.description("Проверка, что после клика соответствующая вкладка становится активной.")
    def test_switch_tabs(self, driver, tab_name, click_tab, wait_active, is_active):
        constructor = ConstructorPage(driver)

        with allure.step(f"Переключиться на вкладку «{tab_name}»"):
            constructor.wait_for_enter_account_button()
            click_tab(constructor)
            wait_active(constructor, 15)

        assert is_active(constructor), f"Вкладка «{tab_name}» не стала активной"
