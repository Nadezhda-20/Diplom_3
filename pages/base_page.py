from __future__ import annotations

import time
from typing import Callable

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


class BasePage:
    DEFAULT_TIMEOUT = 15

    def __init__(self, driver: WebDriver):
        self._driver = driver

   
    @allure.step("Открыть страницу: {url}")
    def open(self, url: str) -> None:
        self._driver.get(url)

    @allure.step("Получить текущий URL")
    def current_url(self) -> str:
        return self._driver.current_url

   
    def _wait(self, timeout: int | float | None = None, poll_frequency: float = 0.2) -> WebDriverWait:
        return WebDriverWait(self._driver, timeout or self.DEFAULT_TIMEOUT, poll_frequency=poll_frequency)

    @allure.step("Ожидание: элемент видим")
    def wait_visible(self, locator, timeout: int | float | None = None) -> WebElement:
       
        elements = self._wait(timeout).until(EC.visibility_of_any_elements_located(locator))
        return elements[0]

    @allure.step("Ожидание: элемент кликабелен")
    def wait_clickable(self, locator, timeout: int | float | None = None) -> WebElement:
        return self._wait(timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание: атрибут {attribute} содержит '{substring}'")
    def wait_attribute_contains(
        self,
        locator,
        attribute: str,
        substring: str,
        timeout: int | float | None = None,
    ) -> None:
        waiter = WebDriverWait(
            self._driver,
            timeout or self.DEFAULT_TIMEOUT,
            poll_frequency=0.2,
            ignored_exceptions=(StaleElementReferenceException, NoSuchElementException),
        )

        waiter.until(
            lambda d: any(
                el.is_displayed() and substring in ((el.get_attribute(attribute) or ""))
                for el in d.find_elements(*locator)
            )
        )

    @allure.step("Ожидание: состояние стабильно {stable_seconds} сек")
    def wait_until_stable(
        self,
        predicate: Callable[[], bool],
        stable_seconds: float = 0.7,
        timeout: int | float | None = None,
        poll_frequency: float = 0.2,
    ) -> None:
        start_true: float | None = None

        waiter = WebDriverWait(
            self._driver,
            timeout or self.DEFAULT_TIMEOUT,
            poll_frequency=poll_frequency,
            ignored_exceptions=(StaleElementReferenceException, NoSuchElementException),
        )

        def _cond(driver) -> bool:
            nonlocal start_true
            ok = bool(predicate())

            if ok:
                if start_true is None:
                    start_true = time.monotonic()
                return (time.monotonic() - start_true) >= stable_seconds

            start_true = None
            return False

        waiter.until(_cond)

  
    @allure.step("Проверка: элемент отображается")
    def is_visible(self, locator) -> bool:
        return any(el.is_displayed() for el in self._driver.find_elements(*locator))

    
    @allure.step("Клик по элементу")
    def click(self, locator, timeout: int | float | None = None) -> None:
        self.wait_clickable(locator, timeout).click()

    @allure.step("Ввод текста в поле")
    def type(self, locator, text: str, timeout: int | float | None = None) -> None:
        el = self.wait_visible(locator, timeout)
        el.clear()
        el.send_keys(text)

    @allure.step("Получить атрибут {attribute}")
    def get_attribute(self, locator, attribute: str, timeout: int | float | None = None) -> str:
        return self.wait_visible(locator, timeout).get_attribute(attribute)

    @allure.step("Получить текст элемента")
    def get_text(self, locator, timeout: int | float | None = None) -> str:
        return self.wait_visible(locator, timeout).text
