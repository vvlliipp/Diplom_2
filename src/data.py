class Url:
    STELLAR_BURGER = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    CHANGE_DATA_USER = '/api/auth/user'
    CREATE_ORDERS = '/api/orders'
    GET_ORDER_SPECIFIC_USER = '/api/orders'



class IdIngredients:
    Bun_1 = '61c0c5a71d1f82001bdaaa6d'
    Sauce = '61c0c5a71d1f82001bdaaa6e'
    Bun_2 = '61c0c5a71d1f82O01bdaaa61'
    Sauce_2 = '61c05a71d1f8201badabum6e'
class Answer:
    answer_user_exists = 'User already exists'
    answer_user_no_email_or_password_or_name = 'Email, password and name are required fields'
    answer_login_invalid_login_password = 'email or password are incorrect'
    answer_no_autorization_change_data = 'You should be authorised'
    answer_invalid_email_change_data = 'User with such email already exists'
    answer_no_ingredients = 'Ingredient ids must be provided'
    answer_no_autorization_get_order = 'You should be authorised'








