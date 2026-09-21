class Url:
    BASE_URL = 'https://stellarburgers.education-services.ru/'
    REGISTR_URL = 'api/auth/register'
    AUTH_URL = 'api/auth/login'
    USER_URL = 'api/auth/user'
    ORDER_URL = 'api/orders'

class Message:
    MESSAGE_ERROR_CREATE_EXIST_USER = 'User already exists'    
    MESSAGE_ERROR_REQURED_FIELD = 'Email, password and name are required fields'
    MESSAGE_ERROR_LOGIN = 'email or password are incorrect'
    MESSAGE_ERROR_AUTHORIZED = 'You should be authorised'
    MESSAGE_ERROR_INGREDIENTS = 'Ingredient ids must be provided'

class Ingridients:
    INGRIDIENTS = ['61c0c5a71d1f82001bdaaa6d',
                   '61c0c5a71d1f82001bdaaa6f',
                   '61c0c5a71d1f82001bdaaa70',
                   '61c0c5a71d1f82001bdaaa71',
                   '61c0c5a71d1f82001bdaaa72',
                   '61c0c5a71d1f82001bdaaa6e',
                   '61c0c5a71d1f82001bdaaa73',
                   '61c0c5a71d1f82001bdaaa74',
                   '61c0c5a71d1f82001bdaaa6c',
                   '61c0c5a71d1f82001bdaaa75',
                   '61c0c5a71d1f82001bdaaa76',
                   '61c0c5a71d1f82001bdaaa77',
                   '61c0c5a71d1f82001bdaaa78',
                   '61c0c5a71d1f82001bdaaa79',
                   '61c0c5a71d1f82001bdaaa7a']
    
    INGRIDIENTS_NON_EXIST = ['1']