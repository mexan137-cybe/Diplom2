import allure
import requests
from data.config import Url, Message
from utils.generators import generate_user_invalid_login_data

class TestLogin:
    @allure.title('Авторизация сущесвующим пользователем')
    def test_success_user_auth_return_code(self, create_user):
        payload = {'email': create_user['user']['email'], 'password': create_user['password']}
        with allure.step("Отправка запроса на авторизацию пользователя в системе"):
            response = requests.post(Url.BASE_URL + Url.AUTH_URL, json= payload)
        assert response.status_code == 200 and response.json()['user']['email'] == payload['email']

    @allure.title('Авторизация с неверной парой логин/пароль')
    def test_failure_user_auth_return_code(self):
        payload = generate_user_invalid_login_data()
        with allure.step("Отправка запроса на авторизацию пользователя в системе"):
            response = requests.post(Url.BASE_URL + Url.AUTH_URL, json= payload)
        assert response.status_code == 401 and response.json()['message'] == Message.MESSAGE_ERROR_LOGIN
