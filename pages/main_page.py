from __future__ import annotations
import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step("Ожидание загрузки страницы профиля")
    def wait_profile_page_load(self) -> None:
        self.wait_visible(MainPageLocators.PROFILE_TEXT, timeout=15)

    @allure.step("Получение значения поля «Email»")
    def get_email_value(self) -> str:
        return self.get_attribute(MainPageLocators.EMAIL_FIELD, "value")

    @allure.step("Получение значения поля «Имя»")
    def get_name_value(self) -> str:
        return self.get_attribute(MainPageLocators.NAME_FIELD, "value")
