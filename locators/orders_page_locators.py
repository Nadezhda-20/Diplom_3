from selenium.webdriver.common.by import By

class OrdersPageLocators:

    # Заголовок Кнопка "Лента заказов"
    orders_line_header = [By.XPATH, ".//h1[text()='Лента заказов']"]
    #5 последних заказов в списке заказов
    last_orders = [By.XPATH, ".//ul[contains(@class,'OrderFeed_list')]/li//p[@class='text text_type_digits-default']"]
    # Номер последнего заказа в списке заказов
    last_order_number = [By.XPATH, ".//ul[contains(@class,'OrderFeed_list')]/li//p[@class='text text_type_digits-default']"]
    # Название последнего заказа в списке заказов
    last_order_name = [By.XPATH, ".//ul[contains(@class,'OrderFeed_list')]/li//h2"]
    #Всплывающее окно с деталями заказа
    order_card = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened') and contains(@class,'Modal_modal')]"]
    # Номер заказа в карточке с деталями заказа
    card_order_number = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened') and contains(@class,'Modal_modal')]//p[@class = 'text text_type_digits-default mb-10 mt-5']"]
    # Название заказа в карточке с деталями заказа
    card_order_name = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened') and contains(@class,'Modal_modal')]//h2"]
    # Счетчик "Выполнено за все время"
    all_orders_counter = [By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"]
    # Счетчик "Выполнено за сегодня"
    today_orders_counter = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"]
    # Номер заказа в разделе "В работе"
    order_in_progress = [By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady') and contains(@class,'OrderFeed_orderList')]/li[@class = 'text text_type_digits-default mb-2']"]
