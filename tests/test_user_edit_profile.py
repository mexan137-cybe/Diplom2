import allure
import pytest
import requests
from data.config import Url, Message
from utils.generators import generate_user_invalid_login_data
from utils.generators import login_user

class TestEditUser:
    @pytest.mark.parametrize('new_field', [{'name': 'Vasya'},{'email': 'me9@mail.eu'}])
    def test_edit_authorized_user_return_data(self, create_user, new_field):
        token = login_user(login = create_user['user']['email'], password = create_user['password'])
        payload = new_field
        headers = {'Authorization': f"{token.get('accessToken')}"}
        responce = requests.patch(Url.BASE_URL + Url.USER_URL, headers= headers, json= payload)
        assert responce.json()['success']
