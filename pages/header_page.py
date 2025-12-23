from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage
import allure

class HeaderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание кликабельности кнопки Личный кабинет')
    def profile_link_wait(self):
        self.wait_clickability_of_element(HeaderPageLocators.user_account_link)

    @allure.step('Клик по кнопке Личный кабинет')
    def profile_link_click(self):
        self.profile_link_wait()
        self.click_on_element(HeaderPageLocators.user_account_link)

    @allure.step('Ожидание кликабельности кнопки Лента заказов')
    def orders_line_button_wait(self):
        self.wait_clickability_of_element(HeaderPageLocators.orders_line)

    @allure.step('Клик по кнопке Лента заказов')
    def orders_line_button_click(self):
        self.orders_line_button_wait()
        self.click_on_element(HeaderPageLocators.orders_line)

    @allure.step('Ожидание кликабельности кнопки Конструктор')
    def constructor_button_wait(self):
        self.wait_clickability_of_element(HeaderPageLocators.constructor)

    @allure.step('Клик по кнопке Конструктор')
    def constructor_button_click(self):
        self.constructor_button_wait()
        self.click_on_element(HeaderPageLocators.constructor)
