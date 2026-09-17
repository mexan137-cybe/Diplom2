import allure
import requests
from data.config import Url, Message
from utils.generators import get_random_ingredients

class TestUserOrders:

    @allure.title("Получение заказов пользователя без авторизации")
    def test_get_order_without_token_return_status_code(self):
        with allure.step("Отправка запроса на получение заказов в системе"):
            response = requests.get(Url.BASE_URL + Url.ORDER_URL)
        assert response.status_code == 401

    @allure.title("Получение заказов пользователя без авторизации возвращает статус успеха")
    def test_get_order_without_token_return_status(self):
        with allure.step("Отправка запроса на получение заказов в системе"):
            response = requests.get(Url.BASE_URL + Url.ORDER_URL)
        assert response.json()['success'] == False

    @allure.title("Получение заказов пользователя без авторизации возвращает сообщение об ошибке")
    def test_get_order_without_token_return_message(self):
        with allure.step("Отправка запроса на получение заказов в системе"):
            response = requests.get(Url.BASE_URL + Url.ORDER_URL)
        assert response.json()['message'] == Message.MESSAGE_ERROR_AUTHORIZED

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_order_with_token_return_code(self,create_user):
        ingridients = get_random_ingredients(4)
        payload = {"ingredients": ingridients}
        token = create_user['accessToken']
        headers = {'Authorization': f"{token}"}
        with allure.step("Отправка запроса на создание заказа в системе"):
            response = requests.post(Url.BASE_URL + Url.ORDER_URL, headers = headers, json = payload)
        with allure.step("Отправка запроса на получение заказов в системе"):
             response = requests.get(Url.BASE_URL + Url.ORDER_URL, headers = headers)
        assert response.status_code == 200

    @allure.title("Получение заказов авторизованного пользователя возвращает статус успеха")
    def test_get_order_with_token_return_succes_code(self,create_user):
        ingridients = get_random_ingredients(4)
        payload = {"ingredients": ingridients}
        token = create_user['accessToken']
        headers = {'Authorization': f"{token}"}
        with allure.step("Отправка запроса на создание заказа в системе"):
            response = requests.post(Url.BASE_URL + Url.ORDER_URL, headers = headers, json = payload)
        with allure.step("Отправка запроса на получение заказов в системе"):
             response = requests.get(Url.BASE_URL + Url.ORDER_URL, headers = headers)
        assert response.json()['success']

    @allure.title("Получение заказов авторизованного пользователя содержит заказы")
    def test_get_order_with_token_return_order(self,create_user):
        ingridients = get_random_ingredients(4)
        payload = {"ingredients": ingridients}
        token = create_user['accessToken']
        headers = {'Authorization': f"{token}"}
        with allure.step("Отправка запроса на создание заказа в системе"):
            response = requests.post(Url.BASE_URL + Url.ORDER_URL, headers = headers, json = payload)
        with allure.step("Отправка запроса на получение заказов в системе"):
             response = requests.get(Url.BASE_URL + Url.ORDER_URL, headers = headers)
        assert len(response.json()['orders']) >= 1