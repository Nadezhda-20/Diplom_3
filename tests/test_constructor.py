import allure
from pages.constructor_page import ConstructorPage

@allure.epic("Stellar Burgers UI")
@allure.feature("Конструктор")
class TestConstructor:
    @allure.title("Проверка: переключение с раздела «Соусы» на раздел «Булки»" )
    @allure.description(
        "Открыта главная страница на разделе «Булки» проверяем переход на раздел «Соусы» и обратно "
        "Проверяем наличие активного CSS-класса у вкладки"
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

    @allure.title("Переключение на раздел «Соусы»")
    @allure.description(
        "Переключение с раздела «Булки» на раздел «Соусы» происходит"
        "Проверяется, что вкладка «Соусы» становится активной после таба"
    )
    def test_switch_sauces(self, driver):
        constructor = ConstructorPage(driver)

        with allure.step("Переключиться на вкладку «Соусы»"):
            constructor.wait_for_enter_account_button()
            constructor.click_sauces_tab()
            constructor.wait_for_sauces_active(15)

        assert constructor.is_sauces_tab_active(), "Вкладка «Соусы» не стала активной"

    @allure.title("Переключение на раздел «Начинки»")
    @allure.description(
        "Пользователь может переключиться на раздел «Начинки»"
        "Проверяется, что вкладка «Начинки» становится активной после таба"
    )
    def test_switch_fillings(self, driver):
        constructor = ConstructorPage(driver)

        with allure.step("Переключиться на вкладку «Начинки»"):
            constructor.wait_for_enter_account_button()
            constructor.click_fillings_tab()
            constructor.wait_for_fillings_active(15)

        assert constructor.is_fillings_tab_active(), "Вкладка «Начинки» не стала активной"
