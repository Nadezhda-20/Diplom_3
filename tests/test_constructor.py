import allure
import pytest

from pages.constructor_page import ConstructorPage


@allure.epic("Stellar Burgers UI")
@allure.feature("Конструктор")
class TestConstructor:
    @pytest.mark.parametrize(
        "from_tab,to_tab",
        [
            ("Булки", "Соусы"),
            ("Соусы", "Начинки"),
            ("Начинки", "Булки"),
        ],
        ids=[
            "Булки→Соусы",
            "Соусы→Начинки",
            "Начинки→Булки",
        ],
    )
    def test_switch_tabs(self, driver, from_tab, to_tab):
        allure.dynamic.title(f"Переключение вкладок: «{from_tab}» → «{to_tab}»")

        constructor = ConstructorPage(driver)

        with allure.step("Дождаться загрузки главной страницы конструктора"):
            constructor.wait_for_enter_account_button()

        with allure.step(f"Убедиться, что активна вкладка «{from_tab}»"):
            constructor.ensure_tab_active(from_tab, timeout_seconds=15)
            assert constructor.is_tab_active(from_tab), f"Вкладка «{from_tab}» не стала активной"

        with allure.step(f"Переключиться на вкладку «{to_tab}»"):
            constructor.ensure_tab_active(to_tab, timeout_seconds=15)
            assert constructor.is_tab_active(to_tab), f"Вкладка «{to_tab}» не стала активной"
