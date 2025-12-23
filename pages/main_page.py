from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Urls, Ingredients
import allure

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание появления заголовка Соберите бургер')
    def constructor_header_wait(self):
        self.wait_visibility_of_element(MainPageLocators.constructor_header)

    @allure.step('Проверка перехода на Главную страницу с Конструктором')
    def check_constructor_transfer(self):
        self.constructor_header_wait()
        current_url = self.get_current_url()
        assert current_url == Urls.CONSTRUCTOR, f'Смена страницы не произошла:{current_url}'

    @allure.step('Ожидание кликабельности ингредиента Флюоресцентная булка')
    def shiny_bun_wait(self):
       self.wait_clickability_of_element(MainPageLocators.shiny_bun_ing)

    @allure.step('Клик по ингредиенту Флюоресцентная булка')
    def shiny_bun_click(self):
        self.shiny_bun_wait()
        self.click_on_element(MainPageLocators.shiny_bun_ing)

    @allure.step('Ожидание видимости окна с деталями')
    def details_card_wait(self):
       self.wait_visibility_of_element(MainPageLocators.details_card)

    @allure.step('Ожидание видимости заголовка Детали ингредиента в окне с деталями')
    def details_card_header_wait(self):
       self.wait_visibility_of_element(MainPageLocators.ing_card_header)

    @allure.step('Проверка что окно с деталями ингредиента открылось и детали совпадают с ингредиентом')
    def check_ingredient_details_card_content(self):
        self.details_card_wait()
        self.details_card_header_wait()
        assert self.get_element_text(MainPageLocators.card_ingredient_name) == Ingredients.BUN and self.get_element_text(MainPageLocators.ing_card_header) == 'Детали ингредиента'

    @allure.step('Ожидание кликабельности кнопки Закрыть в окне с деталями ингредиента')
    def details_card_close_button_wait(self):
       self.wait_clickability_of_element(MainPageLocators.ing_card_close_button)

    @allure.step('Клик по кнопке Закрыть в окне с деталями ингредиента')
    def details_card_close_button_click(self):
        self.details_card_close_button_wait()
        self.click_on_element(MainPageLocators.ing_card_close_button)

    @allure.step('Ожидание исчезновения заголовка Детали ингредиента')
    def wait_ing_details_header_disappear(self):
        self.wait_element_disappear(MainPageLocators.ing_card_header)

    @allure.step('Проверка исчезновения открытого окна с деталями ингредиента из DOM')
    def check_ingredient_details_card_close(self):        
        self.wait_element_disappear(MainPageLocators.details_card)

    @allure.step('Перетащить Флюоресцентную булку в конструктор')
    def choose_shiny_bun(self):
        self.shiny_bun_wait()
        self.drag_drop_element(MainPageLocators.shiny_bun_ing, MainPageLocators.burger_constructor)

    @allure.step('Ожидание что каунтер ингредиента Флюоресцентная булка изменился')
    def wait_counter_change(self):
        self.wait_elem_text_change(MainPageLocators.shiny_bun_counter, '0')

    @allure.step('Проверка что каунтер ингредиента Флюоресцентная булка изменился')
    def check_counter_change(self):
        self.wait_counter_change()
        counter = self.get_element_text(MainPageLocators.shiny_bun_counter)
        assert counter == '2', f'Каунтер не изменился корректно: {counter}'

    @allure.step('Ожидание кликабельности соуса')
    def spicy_sauce_wait(self):
        self.wait_clickability_of_element(MainPageLocators.spicy_sauce)

    @allure.step('Перетащить соус в конструктор')
    def choose_sauce(self):
        self.spicy_sauce_wait()
        self.drag_drop_element(MainPageLocators.spicy_sauce, MainPageLocators.burger_constructor_basket)

    @allure.step('Ожидание кликабельности начинки')
    def filling_wait(self):
        self.wait_clickability_of_element(MainPageLocators.mollusk_meat)

    @allure.step('Перетащить начинку в конструктор')
    def choose_filling(self):
        self.filling_wait()
        self.drag_drop_element(MainPageLocators.mollusk_meat, MainPageLocators.burger_constructor_basket)

    @allure.step('Формирование заказа из трех ингредиентов')
    def make_burger(self):
        self.choose_shiny_bun()
        self.choose_sauce()
        self.choose_filling()

    @allure.step('Ожидание кликабельности кнопки Оформить заказ')
    def submit_order_button_wait(self):
        self.wait_clickability_of_element(MainPageLocators.submit_order_button)

    @allure.step('Клик по кнопке Оформить заказ')
    def submit_order_button_click(self):
        self.submit_order_button_wait()
        self.click_on_element(MainPageLocators.submit_order_button)

    @allure.step('Создание заказа и клик по кнопке Оформить заказ')
    def submit_order(self):
        self.make_burger()
        self.submit_order_button_click()
        self.order_number_wait()

    @allure.step('Ожидание появления номера заказа в окне подтверждения заказа')
    def order_number_wait(self):
        self.details_card_wait()
        self.wait_elem_text_change(MainPageLocators.order_number, '9999')

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        self.order_number_wait()
        return self.get_element_text(MainPageLocators.order_number)

    @allure.step('Проверка что в окне с деталями заказа вернулся номер заказа')
    def check_order_number_assigned(self, order):
        assert len(order) !=0 and order.isdigit(), f'Номер заказа присвоен некорректно: {order}'

    @allure.step('Переход на главную страницу с Конструктором заказов')
    def transfer_to_main_page(self):
        self.change_url(Urls.CONSTRUCTOR)
        self.constructor_header_wait()
