class Urls:
    
    URL_SERVICE = 'https://stellarburgers.education-services.ru'
    # Страница Авторизации
    LOGIN = URL_SERVICE + '/login'
    # Страница Восстановление пароля
    FORGOT_PASSWORD = URL_SERVICE + '/forgot-password'
    # Страница Сброс пароля
    RESET_PASSWORD = URL_SERVICE + '/reset-password'
    # Личный кабинет
    PROFILE = URL_SERVICE + '/account/profile'
    # История заказов в Личном кабинете
    HISTORY =  URL_SERVICE + '/account/order-history'
    # Главная страница с Конструктором
    CONSTRUCTOR = URL_SERVICE + '/'
    # Страница Лента заказов
    ORDERS =  URL_SERVICE + '/feed'

class Endpoints:

    # Создание пользователя
    USER_REGISTER = '/api/auth/register'
    # Работа с данными пользователя
    USER = '/api/auth/user'
    # Получение данных об ингредиентах
    INGREDIENTS = '/api/ingredients'
    # Создание заказа
    ORDER = '/api/orders'

class Ingredients:

    BUN = 'Флюоресцентная булка R2-D3'

class User:

    email = 'example@email.com'
