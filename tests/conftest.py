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
    if user['success']:
        return user
