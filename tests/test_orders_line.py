from pages.header_page import HeaderPage
from pages.profile_page import ProfilePage
from pages.orders_page import OrdersPage
from pages.main_page import MainPage
import allure

class TestOrdersLine:

    @allure.title('Появление всплывающего окна с деталями заказа при клике на заказ в Ленте заказов')
    @allure.step("Шаги теста")
    def test_orders_line_on_click_order_in_line_order_details_card_opens(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        orders_page.last_order_card_open()
        orders_page.check_card_order_number_and_name()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.step("Шаги теста")
    def test_orders_line_profile_history_orders_present_in_orders_line(self, driver, submit_order, upload_tokens_to_session):
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        profile_page = ProfilePage(driver)
        profile_page.transfer_to_history_page()
        order = profile_page.get_history_page_order_number()
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        orders_page.check_order_present_in_last_5_orders_in_orders_line(order)

    @allure.title('Счётчик "Выполнено за всё время" при создании нового заказа увеличивается')
    @allure.step("Шаги теста")
    def test_orders_line_order_created_all_orders_counter_increases(self, driver, upload_tokens_to_session):
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        all_orders_before = orders_page.get_all_orders()
        main_page = MainPage(driver)
        main_page.transfer_to_main_page()
        main_page.submit_order()
        orders_page.transfer_to_orders_page()
        orders_page.check_all_orders_counter_increased(all_orders_before)

    @allure.title('Счётчик "Выполнено за сегодня" при создании нового заказа увеличивается')
    @allure.step("Шаги теста")
    def test_orders_line_order_created_today_orders_counter_increases(self, driver, upload_tokens_to_session):
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        today_orders_before = orders_page.get_today_orders()
        main_page = MainPage(driver)
        main_page.transfer_to_main_page()
        main_page.submit_order()
        orders_page.transfer_to_orders_page()
        orders_page.check_today_orders_counter_increased(today_orders_before)

    @allure.title('Заказ оформлен, его номер появляется в разделе "В работе"')
    @allure.step("Шаги теста")
    def test_orders_line_order_created_order_appears_in_orders_in_progress_section(self, driver, upload_tokens_to_session):
        main_page = MainPage(driver)
        main_page.submit_order()
        order = main_page.get_order_number()
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        orders_page.check_order_in_order_in_progress_section(order)
