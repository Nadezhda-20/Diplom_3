from selenium.webdriver.common.by import By

class RestorePasswordPageLocators:

    # Кнопка "Восстановить"
    restore_password_button = [By.XPATH, ".//button[text()='Восстановить']"]
    # Поле ввода email
    email_field = [By.XPATH, ".//label[text()='Email']/following-sibling::input"]
    # Кнопка "Сохранить"
    save_password_button = [By.XPATH, ".//button[text()='Сохранить']"]
    # Кнопка показать/скрыть пароль в поле password
    show_password_button = [By.XPATH, ".//div[@class = 'input__icon input__icon-action']"]
    # Ярлык поля ввода нового пароля
    pass_input_label = [By.XPATH, ".//label[text()='Пароль']"]
    # Контейнер поля ввода нового пароля
    pass_input_div = [By.XPATH, ".//label[text()='Пароль']/parent::div"]
