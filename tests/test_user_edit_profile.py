import allure
import pytest
import requests
from data.config import Url, Message

class TestEditUser:
    @pytest.mark.parametrize('new_field', [{'name': 'Vasya'},{'email': 'me45@mail.eu'}])
    @allure.title('Изменение профиля пользователя с авторизацией')
    def test_edit_authorized_user_return_data(self, create_user, new_field):
        token = create_user['accessToken']
        payload = new_field
        headers = {'Authorization': f"{token}"}
        with allure.step("Отправка запроса на изменения профиля пользователя в системе"):
            responce = requests.patch(Url.BASE_URL + Url.USER_URL, headers= headers, json= payload)
        assert responce.json()['success']

    @pytest.mark.parametrize('new_field', [{'name': 'Vasya'},{'email': 'me45@mail.eu'}])
    @allure.title('Изменение профиля пользователя без авторизации')
    def test_edit_no_authorized_user_return_code(self, new_field):
        payload = new_field
        with allure.step("Отправка запроса на изменение профиля пользователя в системе"):
            responce = requests.patch(Url.BASE_URL + Url.USER_URL, json= payload)
        assert responce.status_code == 401 and responce.json()['message'] == Message.MESSAGE_ERROR_AUTHORIZED
        