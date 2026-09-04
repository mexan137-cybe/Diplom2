from faker import Faker
import requests
import string
import random
from data.config import Url

fake = Faker('ru_RU')

def generate_user_registration_data():
    data = {'email': fake.email(), 'password': fake.password(), 'name': fake.first_name()}
    return data

def generate_user_invalid_login_data():
    data = {'login': fake.email(), 'password': fake.password()}
    return data

def login_user(login, password):
    payload = {'email': login, 'password': password}
    response = requests.post(Url.BASE_URL + Url.AUTH_URL, json= payload)
    if response.json()['success']:
        token = {'accessToken': response.json()['accessToken'], 'refreshToken': response.json()['refreshToken']}
        return token