from __future__ import annotations

import allure

from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    TAB_BUNS = "Булки"
    TAB_SAUCES = "Соусы"
    TAB_FILLINGS = "Начинки"

    _TAB_LOCATORS = {
        TAB_BUNS: ConstructorPageLocators.BUNS_TAB,
        TAB_SAUCES: ConstructorPageLocators.SAUCES_TAB,
        TAB_FILLINGS: ConstructorPageLocators.FILLINGS_TAB,
    }

    def _tab_locator(self, tab_name: str):
        if tab_name not in self._TAB_LOCATORS:
            raise ValueError(
                f"Неизвестная вкладка: {tab_name}. Ожидается одна из: {', '.join(self._TAB_LOCATORS.keys())}"
            )
        return self._TAB_LOCATORS[tab_name]

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

    @allure.step("Получить атрибут class у вкладки «{tab_name}»")
    def tab_class(self, tab_name: str) -> str:
        return self.get_attribute(self._tab_locator(tab_name), "class") or ""

    def is_tab_active(self, tab_name: str) -> bool:
        return ConstructorPageLocators.ACTIVE_TAB_CLASS_SUBSTRING in self.tab_class(tab_name)

    @allure.step("Открыть вкладку «{tab_name}»")
    def open_tab(self, tab_name: str) -> None:
        if self.is_tab_active(tab_name):
            return
        self.click(self._tab_locator(tab_name), timeout=10)

    @allure.step("Ожидание, что вкладка «{tab_name}» станет активной (стабильно)")
    def wait_tab_active(self, tab_name: str, timeout_seconds: int = 15) -> None:
        other_tabs = [t for t in self._TAB_LOCATORS.keys() if t != tab_name]
        self.wait_until_stable(
            lambda: self.is_tab_active(tab_name) and all(not self.is_tab_active(t) for t in other_tabs),
            stable_seconds=0.7,
            timeout=timeout_seconds,
        )

    @allure.step("Сделать вкладку «{tab_name}» активной")
    def ensure_tab_active(self, tab_name: str, timeout_seconds: int = 15) -> None:
        if not self.is_tab_active(tab_name):
            self.open_tab(tab_name)
        self.wait_tab_active(tab_name, timeout_seconds=timeout_seconds)

    @allure.step("Нажатие на вкладку «Булки»")
    def click_buns_tab(self) -> None:
        self.open_tab(self.TAB_BUNS)

    @allure.step("Нажатие на вкладку «Соусы»")
    def click_sauces_tab(self) -> None:
        self.open_tab(self.TAB_SAUCES)

    @allure.step("Нажатие на вкладку «Начинки»")
    def click_fillings_tab(self) -> None:
        self.open_tab(self.TAB_FILLINGS)

    @allure.step("Ожидание, что вкладка «Булки» станет активной (стабильно)")
    def wait_for_buns_active(self, timeout_seconds: int = 15) -> None:
        self.wait_tab_active(self.TAB_BUNS, timeout_seconds=timeout_seconds)

    @allure.step("Ожидание, что вкладка «Соусы» станет активной (стабильно)")
    def wait_for_sauces_active(self, timeout_seconds: int = 15) -> None:
        self.wait_tab_active(self.TAB_SAUCES, timeout_seconds=timeout_seconds)

    @allure.step("Ожидание, что вкладка «Начинки» станет активной (стабильно)")
    def wait_for_fillings_active(self, timeout_seconds: int = 15) -> None:
        self.wait_tab_active(self.TAB_FILLINGS, timeout_seconds=timeout_seconds)

    def is_buns_tab_active(self) -> bool:
        return self.is_tab_active(self.TAB_BUNS)

    def is_sauces_tab_active(self) -> bool:
        return self.is_tab_active(self.TAB_SAUCES)

    def is_fillings_tab_active(self) -> bool:
        return self.is_tab_active(self.TAB_FILLINGS)
