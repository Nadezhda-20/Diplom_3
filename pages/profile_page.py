from __future__ import annotations
import allure
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage

class ProfilePage(BasePage):
    @allure.step("Ожидание загрузки страницы «Восстановление пароля»")
    def wait_profile_page_load(self) -> None:
        self.wait_visible(ProfilePageLocators.HEADING, timeout=15)

    @allure.step("Нажатие на ссылку «Войти» под формой восстановления")
    def click_remembered_password(self) -> None:
        self.click(ProfilePageLocators.REMEMBERED_PASSWORD_LINK)
