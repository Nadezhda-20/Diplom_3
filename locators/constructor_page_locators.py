from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, ".//button[normalize-space(text())='Войти в аккаунт']")
    CHECKOUT_BUTTON = (By.XPATH, ".//button[normalize-space(text())='Оформить заказ']")

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH,
        ".//p[contains(@class,'AppHeader_header__linkText') and contains(@class,'ml-2') and normalize-space(text())='Личный Кабинет']",
    )

    BUNS_TAB = (By.XPATH,
        "//section[contains(@class,'BurgerIngredients_ingredients')]"
        "//div[contains(@class,'tab_tab')][.//span[normalize-space(text())='Булки']]",
    )
    SAUCES_TAB = (By.XPATH,
        "//section[contains(@class,'BurgerIngredients_ingredients')]"
        "//div[contains(@class,'tab_tab')][.//span[normalize-space(text())='Соусы']]",
    )
    FILLINGS_TAB = (By.XPATH,
        "//section[contains(@class,'BurgerIngredients_ingredients')]"
        "//div[contains(@class,'tab_tab')][.//span[normalize-space(text())='Начинки']]",
    )

    ACTIVE_TAB_CLASS_SUBSTRING = "tab_tab_type_current"
