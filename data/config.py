class Url:
    BASE_URL = 'https://stellarburgers.education-services.ru/'
    REGISTR_URL = 'api/auth/register'
    AUTH_URL = 'api/auth/login'
    USER_URL = 'api/auth/user'

class Message:
    MESSAGE_ERROR_CREATE_EXIST_USER = 'User already exists'    
    MESSAGE_ERROR_REQURED_FIELD = 'Email, password and name are required fields'
    MESSAGE_ERROR_LOGIN = 'email or password are incorrect'
    MESSAGE_ERROR_AUTHORIZED = 'You should be authorised'