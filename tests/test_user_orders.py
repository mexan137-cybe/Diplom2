import allure
import requests
from data.config import Url, Message
from utils.generators import get_random_ingredients

class TestUserOrders:

    @allure.title("Получение заказов пользователя без авторизации")
    def test_get_order_without_token_return_status_code(self):
        with allure.step("Отправка запроса на получение заказов в системе"):
            response = requests.get(Url.BASE_URL + Url.ORDER_URL)
        assert response.status_code == 401 and response.json()['message'] == Message.MESSAGE_ERROR_AUTHORIZED and response.json()['success'] == False

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
        assert response.status_code == 200 and response.json()['success'] and len(response.json()['orders']) >= 1
