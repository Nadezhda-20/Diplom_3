# Diplom_3 — Stellar Burgers UI autotests

UI автотесты для Stellar Burgers: https://stellarburgers.education-services.ru

## Стек
- Python + pytest
- Selenium
- Allure

## Структура
- `tests/` — тесты
- `pages/` — Page Objects
- `locators/` — локаторы (1:1 со страницами)
- `utils/` — константы/фабрика драйверов
- `api/` — API шаги (создание/удаление тестового пользователя)
- `data/` — тестовые данные

## Установка
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
# Diplom_3
