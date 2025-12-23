from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.profile_page import ProfilePage
from pages.orders_page import OrdersPage
import allure

class TestOrderCreation:

    @allure.title('Переход неавторизованного пользователя на Главную страницу с Конструктором по клику на кнопку «Конструктор» в шапке страницы')
    @allure.step("Шаги теста")
    def test_order_creation_user_not_authorized_on_click_constructor_button_constructor_opens(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        header_page.constructor_button_click()
        main_page.check_constructor_transfer()

    @allure.title('Переход авторизованного пользователя на Главную страницу с Конструктором по клику на кнопку «Конструктор» в шапке страницы')
    @allure.step("Шаги теста")
    def test_order_creation_user_authorized_on_click_constructor_button_constructor_opens(self, driver, upload_tokens_to_session):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        header_page.profile_link_click()
        profile_page = ProfilePage(driver)
        profile_page.profile_tab_wait()
        header_page.constructor_button_click()
        main_page.check_constructor_transfer()

    @allure.title('Переход неавторизованного пользователя на страницу «Лента заказов» по клику на кнопку «Лента заказов» в шапке страницы')
    @allure.step("Шаги теста")
    def test_order_creation_user_not_authorized_on_click_orders_line_button_orders_page_opens(self, driver):
        header_page = HeaderPage(driver)
        orders_page = OrdersPage(driver)
        header_page.orders_line_button_click()
        orders_page.check_orders_page_transfer()

    @allure.title('Переход авторизованного пользователя на страницу «Лента заказов» по клику на кнопку «Лента заказов» в шапке страницы')
    @allure.step("Шаги теста")
    def test_order_creation_user_authorized_on_click_orders_line_button_orders_page_opens(self, driver, upload_tokens_to_session):
        header_page = HeaderPage(driver)
        orders_page = OrdersPage(driver)
        profile_page = ProfilePage(driver)
        header_page.profile_link_click()
        profile_page.profile_tab_wait()
        header_page.orders_line_button_click()
        orders_page.check_orders_page_transfer()

    @allure.title('Появление всплывающего окна с деталями ингредиента при клике на ингредиент')
    @allure.step("Шаги теста")
    def test_order_creation_on_click_ingredient_ingredient_details_card_opens(self, driver):
        main_page = MainPage(driver)
        main_page.shiny_bun_click()
        main_page.check_ingredient_details_card_content()

    @allure.title('Всплывающее окно с деталями ингредиента закрывается кликом по крестику')
    @allure.step("Шаги теста")
    def test_order_creation_on_click_ingredient_details_card_close_button_card_closes(self, driver):
        main_page = MainPage(driver)
        main_page.shiny_bun_click()
        main_page.details_card_close_button_click()
        main_page.check_ingredient_details_card_close()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.step("Шаги теста")
    def test_order_creation_on_add_ingredient_to_constructor_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.choose_shiny_bun()
        main_page.check_counter_change()

    @allure.title('Создание заказа авторизованным пользователем')
    @allure.step("Шаги теста")
    def test_order_creation_user_authorized_constructor_filled_and_submitted_order_created(self, driver, upload_tokens_to_session):
        main_page = MainPage(driver)
        main_page.submit_order()
        order = main_page.get_order_number()
        main_page.check_order_number_assigned(order)
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        orders_page.check_order_present_in_last_5_orders_in_orders_line(order)
