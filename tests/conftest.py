import pytest
import requests
from data.config import Url
from utils.generators import generate_user_registration_data

@pytest.fixture
def create_user():
    payload = generate_user_registration_data()
    response = requests.post(Url.BASE_URL + Url.REGISTR_URL, json= payload)
    user = response.json()
    user['password'] = payload['password']
    if not user.get('success'):
        pytest.fail(f'Не удалось создать пользователя')
    yield user
    token = user.get('accessToken')
    headers = {'Authorization': token}
    requests.delete(Url.BASE_URL + Url.USER_URL, headers= headers)

@pytest.fixture
def delete_user():
    tokens = []
    yield tokens
    for token in tokens:
        if token:
            headers = {'Authorization': token}
            requests.delete(Url.BASE_URL + Url.USER_URL, headers= headers)
