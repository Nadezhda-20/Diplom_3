from selenium.webdriver.common.by import By

class MainPageLocators:
    # Заголовок "Соберите бургер"
    constructor_header = [By.XPATH, ".//h1[text()='Соберите бургер']"]
    #Ингредиент Флюоресцентная булка
    shiny_bun_ing = [By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']"]
    #Всплывающее окно с деталями
    details_card = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened') and contains(@class,'Modal_modal')]"]
    # Заголовок окна с деталями ингредиента Детали ингредиента
    ing_card_header = [By.XPATH, ".//h2[text()='Детали ингредиента']"]
    #Название ингредиента в окне с деталями ингредиента
    card_ingredient_name = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened') and contains(@class,'Modal_modal')]//p"]
    # Кнопк Закрыть в окне с деталями ингредиента
    ing_card_close_button = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened') and contains(@class,'Modal_modal')]//button"]
    #Конструктор бургера
    burger_constructor = [By.XPATH, ".//span[text() = 'Перетяните булочку сюда (верх)']"]
    burger_constructor_basket = [By.XPATH, ".//ul[contains(@class,'BurgerConstructor_basket__list')]"]
    #Каунтер в карточке ингредиента Флюоресцентная булка R2-D3
    shiny_bun_counter = [By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']/parent::a//p"]
    #Ингредиент Мясо бессмертных моллюсков Protostomia
    mollusk_meat = [By.XPATH, ".//img[@alt = 'Мясо бессмертных моллюсков Protostomia']"]
    #Ингредиент Соус Spicy-X
    spicy_sauce = [By.XPATH, ".//img[@alt = 'Соус Spicy-X']"]
    # Кнопка "Оформить заказ"
    submit_order_button = [By.XPATH, ".//button"]
    # Номер заказа в окне с деталями заказа
    order_number = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened') and contains(@class,'Modal_modal')]//h2"]
