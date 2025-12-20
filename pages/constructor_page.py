from __future__ import annotations
import allure
from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage

class ConstructorPage(BasePage):
    @allure.step("Ожидание появления кнопки «Войти в аккаунт»")
    def wait_for_enter_account_button(self) -> None:
        self.wait_visible(ConstructorPageLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step("Нажатие на кнопку «Войти в аккаунт»")
    def click_enter_account_button(self) -> None:
        self.click(ConstructorPageLocators.ENTER_ACCOUNT_BUTTON, timeout=10)

    @allure.step("Ожидание появления кнопки «Оформить заказ»")
    def wait_checkout_button(self) -> None:
        self.wait_visible(ConstructorPageLocators.CHECKOUT_BUTTON, timeout=15)

    @allure.step("Ожидание появления кнопки «Личный Кабинет»")
    def wait_for_personal_account_button(self) -> None:
        self.wait_visible(ConstructorPageLocators.PERSONAL_ACCOUNT_BUTTON, timeout=15)

    @allure.step("Нажатие на кнопку «Личный Кабинет»")
    def click_personal_account_button(self) -> None:
        self.click(ConstructorPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Нажатие на вкладку «Булки»")
    def click_buns_tab(self) -> None:
        self.click(ConstructorPageLocators.BUNS_TAB)

    @allure.step("Нажатие на вкладку «Соусы»")
    def click_sauces_tab(self) -> None:
        self.click(ConstructorPageLocators.SAUCES_TAB)

    @allure.step("Нажатие на вкладку «Начинки»")
    def click_fillings_tab(self) -> None:
        self.click(ConstructorPageLocators.FILLINGS_TAB)

    @allure.step("Получение атрибута class у вкладки «Булки»")
    def buns_tab_class(self) -> str:
        return self.get_attribute(ConstructorPageLocators.BUNS_TAB, "class")

    @allure.step("Получение атрибута class у вкладки «Соусы»")
    def sauces_tab_class(self) -> str:
        return self.get_attribute(ConstructorPageLocators.SAUCES_TAB, "class")

    @allure.step("Получение атрибута class у вкладки «Начинки»")
    def fillings_tab_class(self) -> str:
        return self.get_attribute(ConstructorPageLocators.FILLINGS_TAB, "class")

    @allure.step("Ожидание, что вкладка «Булки» станет активной (стабильно)")
    def wait_for_buns_active(self, timeout_seconds: int = 15) -> None:
        self.wait_until_stable(
            lambda: self.is_buns_tab_active()
            and not self.is_sauces_tab_active()
            and not self.is_fillings_tab_active(),
            stable_seconds=0.7,
            timeout=timeout_seconds,
        )

    @allure.step("Ожидание, что вкладка «Соусы» станет активной (стабильно)")
    def wait_for_sauces_active(self, timeout_seconds: int = 15) -> None:
        self.wait_until_stable(
            lambda: self.is_sauces_tab_active() and not self.is_buns_tab_active(),
            stable_seconds=0.7,
            timeout=timeout_seconds,
        )

    @allure.step("Ожидание, что вкладка «Начинки» станет активной (стабильно)")
    def wait_for_fillings_active(self, timeout_seconds: int = 15) -> None:
        self.wait_until_stable(
            lambda: self.is_fillings_tab_active() and not self.is_buns_tab_active(),
            stable_seconds=0.7,
            timeout=timeout_seconds,
        )
  
    def is_buns_tab_active(self) -> bool:
        return ConstructorPageLocators.ACTIVE_TAB_CLASS_SUBSTRING in self.buns_tab_class()

    def is_sauces_tab_active(self) -> bool:
        return ConstructorPageLocators.ACTIVE_TAB_CLASS_SUBSTRING in self.sauces_tab_class()

    def is_fillings_tab_active(self) -> bool:
        return ConstructorPageLocators.ACTIVE_TAB_CLASS_SUBSTRING in self.fillings_tab_class()
