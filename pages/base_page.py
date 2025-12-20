from __future__ import annotations
import time
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
)

class BasePage:
    DEFAULT_TIMEOUT = 15

    def __init__(self, driver: WebDriver):
        self._driver = driver
   
    def open(self, url: str) -> None:
        self._driver.get(url)

    def current_url(self) -> str:
        return self._driver.current_url
  
    def _wait(self, timeout: int | float | None = None) -> WebDriverWait:
        return WebDriverWait(self._driver, timeout or self.DEFAULT_TIMEOUT)

    def wait_visible(self, locator, timeout: int | float | None = None) -> WebElement:
       
        elements = self._wait(timeout).until(EC.visibility_of_any_elements_located(locator))
        return elements[0]

    def wait_clickable(self, locator, timeout: int | float | None = None) -> WebElement:
        return self._wait(timeout).until(EC.element_to_be_clickable(locator))

    def wait_attribute_contains(
        self,
        locator,
        attribute: str,
        substring: str,
        timeout: int | float | None = None,
    ) -> None:
        

        def _predicate(driver) -> bool:
            try:
                el = self.wait_visible(locator, timeout=1)
                value = el.get_attribute(attribute) or ""
                return substring in value
            except StaleElementReferenceException:
                return False
            except Exception:
                return False

        self._wait(timeout).until(_predicate)

    def wait_until_stable(
        self,
        predicate,
        stable_seconds: float = 0.7,
        timeout: int | float | None = None,
        poll_frequency: float = 0.2,
    ) -> None:
        
        start_true: float | None = None

        def _cond(driver) -> bool:
            nonlocal start_true
            try:
                ok = bool(predicate())
            except Exception:
                ok = False

            if ok:
                if start_true is None:
                    start_true = time.monotonic()
                return (time.monotonic() - start_true) >= stable_seconds

            start_true = None
            return False

        WebDriverWait(
            self._driver,
            timeout or self.DEFAULT_TIMEOUT,
            poll_frequency=poll_frequency,
        ).until(_cond)
   
    def is_visible(self, locator, timeout: int | float | None = 3) -> bool:
        try:
            self._wait(timeout).until(EC.visibility_of_any_elements_located(locator))
            return True
        except Exception:
            return False
   
    @allure.step("Клик по элементу")
    def click(self, locator, timeout: int | float | None = None) -> None:
        try:
            self.wait_clickable(locator, timeout).click()
        except ElementClickInterceptedException:           
            el = self.wait_visible(locator, timeout)
            self._driver.execute_script("arguments[0].click();", el)

    @allure.step("Ввод текста в поле")
    def type(self, locator, text: str, timeout: int | float | None = None) -> None:
        el = self.wait_visible(locator, timeout)
        el.clear()
        el.send_keys(text)

    def get_attribute(self, locator, attribute: str, timeout: int | float | None = None) -> str:
        return self.wait_visible(locator, timeout).get_attribute(attribute)

    def get_text(self, locator, timeout: int | float | None = None) -> str:
        return self.wait_visible(locator, timeout).text
