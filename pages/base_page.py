import time
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по URL")
    def change_url(self, url: str):
        self.driver.get(url)

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Максимизировать окно браузера")
    def maximize_window(self):
        self.driver.maximize_window()

    @allure.step("Установить размер окна браузера: {width}x{height}")
    def set_window_size(self, width: int = 1920, height: int = 1080):
        self.driver.set_window_size(width, height)

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script: str, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Установить значение в localStorage: {key}")
    def set_local_storage_item(self, key: str, value: str):
        self.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    @allure.step("Очистить localStorage")
    def clear_local_storage(self):
        self.execute_script("window.localStorage.clear();")

    @allure.step("Удалить все cookies")
    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    @allure.step("Закрыть браузер")
    def quit(self):
        self.driver.quit()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Нормализовать номер заказа")
    def normalize_order_number(self, value) -> str:
        s = str(value).strip()
        s = s.replace("#", "").strip()
        s = s.lstrip("0") or "0"
        return s

    @allure.step("Ожидание видимости элемента")
    def wait_visibility_of_element(self, locator, timeout: int = 15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание присутствия элемента в DOM")
    def wait_presence_of_element(self, locator, timeout: int = 15):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_clickability_of_element(self, locator, timeout: int = 15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Прокрутить к элементу (центр экрана)")
    def scroll_into_view(self, element):
        self.execute_script("arguments[0].scrollIntoView({block:'center', inline:'center'});", element)
        # небольшой сдвиг вверх из-за фиксированного хедера/оверлея
        self.execute_script("window.scrollBy(0, -120);")

    @allure.step("Клик по элементу (устойчивый)")
    def click_on_element(self, locator, timeout: int = 15, poll: float = 0.2):
        """
        Устойчивый клик без time.sleep:
        - пробуем обычный клик по кликабельному элементу
        - если перехват/протухание — пробуем ActionChains
        - если за timeout не получилось — финальный JS click
        """

        def _attempt(_driver):           
            try:
                element = self.wait_clickability_of_element(locator, timeout=3)
                self.scroll_into_view(element)
                element.click()
                return element
            except (ElementClickInterceptedException, StaleElementReferenceException):
                pass
           
            try:
                element = self.wait_presence_of_element(locator, timeout=3)
                self.scroll_into_view(element)
                ActionChains(self.driver).move_to_element(element).pause(0.05).click().perform()
                return element
            except (ElementClickInterceptedException, StaleElementReferenceException):
                return False

        try:
            return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(_attempt)
        except TimeoutException:        
            element = self.wait_presence_of_element(locator, timeout)
            self.scroll_into_view(element)
            self.execute_script("arguments[0].click();", element)
            return element

    @allure.step("Ввод текста в поле")
    def send_keys_to_input(self, locator, text: str, timeout: int = 15, clear: bool = True):
        element = self.wait_visibility_of_element(locator, timeout)
        if clear:
            element.clear()
        element.send_keys(text)
        return element

    @allure.step("Получение текста элемента")
    def get_element_text(self, locator, timeout: int = 15) -> str:
        element = self.wait_visibility_of_element(locator, timeout)
        return element.text

    @allure.step("Получение класса элемента")
    def get_element_class(self, locator, timeout: int = 15) -> str:
        element = self.wait_presence_of_element(locator, timeout)
        return element.get_attribute("class") or ""

    @allure.step("Найти элементы")
    def find_elements(self, locator, timeout: int = 15):
        self.wait_presence_of_element(locator, timeout)
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание исчезновения элемента")
    def wait_element_disappear(self, locator, timeout: int = 15):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Ожидание изменения ссылки (URL)")
    def wait_link_changes(self, old_url: str, timeout: int = 15):
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url != old_url)

    @allure.step("Ожидание изменения текста элемента")
    def wait_elem_text_change(self, locator, old_text: str, timeout: int = 15):
        WebDriverWait(self.driver, timeout).until(lambda d: self.get_element_text(locator) != old_text)

    @allure.step("Ожидание изменения значения элемента (value)")
    def wait_elem_value_changes(self, locator, old_value: str, timeout: int = 15):
        def _value():
            element = self.wait_presence_of_element(locator)
            return element.get_attribute("value") or ""

        WebDriverWait(self.driver, timeout).until(lambda d: _value() != old_value)

    @allure.step("Ожидать видимый элемент (alias)")
    def wait_visible(self, locator, timeout: int = 15):
        return self.wait_visibility_of_element(locator, timeout)

    @allure.step("Кликнуть (alias)")
    def click(self, locator, timeout: int = 15):
        return self.click_on_element(locator, timeout)

    @allure.step("Получить атрибут элемента (alias)")
    def get_attribute(self, locator, name: str, timeout: int = 15):
        element = self.wait_presence_of_element(locator, timeout)
        return element.get_attribute(name)

    @allure.step("Дождаться стабильности условия")
    def wait_until_stable(self, condition, timeout: int = 10, stable_seconds: float = 0.5, poll: float = 0.1):
        """
        Ждём, чтобы condition() возвращало True непрерывно stable_seconds.
        Без time.sleep: используем WebDriverWait с poll_frequency.
        """
        state = {"stable_from": None}

        def _check(_driver):
            try:
                ok = bool(condition())
            except Exception:
                ok = False

            now = time.monotonic()
            if ok:
                if state["stable_from"] is None:
                    state["stable_from"] = now
                return (now - state["stable_from"]) >= stable_seconds

            state["stable_from"] = None
            return False

        WebDriverWait(self.driver, timeout, poll_frequency=poll).until(_check)

    @allure.step("Перетащить элемент")
    def drag_drop_element(self, source_locator, target_locator, timeout: int = 15):
        source_element = self.wait_visibility_of_element(source_locator, timeout)
        target_element = self.wait_visibility_of_element(target_locator, timeout)

        if getattr(self.driver, "name", "").lower() == "firefox":
            self.execute_script(
                """
                function createEvent(type) {
                    var event = document.createEvent('CustomEvent');
                    event.initCustomEvent(type, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function(key, value) { this.data[key] = value; },
                        getData: function(key) { return this.data[key]; }
                    };
                    return event;
                }
                function dispatchEvent(element, event, transferData) {
                    if (transferData !== undefined) {
                        event.dataTransfer = transferData;
                    }
                    if (element.dispatchEvent) {
                        element.dispatchEvent(event);
                    } else if (element.fireEvent) {
                        element.fireEvent('on' + event.type, event);
                    }
                }

                var source = arguments[0];
                var target = arguments[1];
                var dragStartEvent = createEvent('dragstart');
                dispatchEvent(source, dragStartEvent);
                var dropEvent = createEvent('drop');
                dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);
                var dragEndEvent = createEvent('dragend');
                dispatchEvent(source, dragEndEvent, dragStartEvent.dataTransfer);
                """,
                source_element,
                target_element,
            )
        else:
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
