import allure
import pytest
import requests
from data.config import Url, Message
from utils.generators import generate_user_registration_data

class TestUserCreate:
    @allure.title("Регистрация уникального пользователя")
    def test_user_register(self):
        payload = generate_user_registration_data()
        with allure.step("Отправка запроса на регистрацию пользователя в системе"):
            response = requests.post(Url.BASE_URL + Url.REGISTR_URL, data = payload)
        assert response.status_code == 200

    @allure.title("Повторная регистрация пользователя возвращает код ошибки")
    def test_user_register_existing_user_return_code(self, create_user):
        payload = {'email': create_user['user']['email'], 'password': create_user['password'], 'name': create_user['user']['email']}
        with allure.step("Отправка запроса на регистрацию пользователя существующего в системе"):
            response = requests.post(Url.BASE_URL + Url.REGISTR_URL, data = payload)
        assert response.status_code == 403

    @allure.title("Повторная регистрация пользователя возвращает сообщение об ошибки")
    def test_user_register_existing_user_return_message(self, create_user):
        payload = {'email': create_user['user']['email'], 'password': create_user['password'], 'name': create_user['user']['email']}
        with allure.step("Отправка запроса на регистрацию пользователя существующего в системе"):
            response = requests.post(Url.BASE_URL + Url.REGISTR_URL, data = payload)
        assert response.json()['message'] == Message.MESSAGE_ERROR_CREATE_EXIST_USER

    @pytest.mark.parametrize('missing_field',['email','password','name'])
    @allure.title("Нельзя создать пользователя без обязательного поля {missing_field}")
    def test_user_register_without_field_return_code(self, missing_field):
        payload = generate_user_registration_data()
        payload.pop(missing_field)
        with allure.step("Отправка запроса на регистрацию пользователя в системе"):
            response = requests.post(Url.BASE_URL + Url.REGISTR_URL, data = payload)
        assert response.status_code == 403

    @pytest.mark.parametrize('missing_field',['email','password','name'])
    @allure.title("Если нет обязательного поля {missing_field} возвращает сообщение об ошибке")
    def test_user_register_without_field_return_message(self, missing_field):
        payload = generate_user_registration_data()
        payload.pop(missing_field)
        with allure.step("Отправка запроса на регистрацию пользователя в системе"):
            response = requests.post(Url.BASE_URL + Url.REGISTR_URL, data = payload)
        assert response.json()['message'] == Message.MESSAGE_ERROR_REQURED_FIELD