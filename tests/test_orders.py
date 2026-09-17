import allure
import pytest
import requests
from data.config import Url, Message, Ingridients
from utils.generators import get_random_ingredients

class TestOrders:
    @allure.title("Успешное создание заказа с авторизацией")
    def test_created_order_with_token_return_status(self, create_user):
        ingridients = get_random_ingredients(4)
        payload = {"ingredients": ingridients}
        token = create_user['accessToken']
        headers = {'Authorization': f"{token}"}
        with allure.step("Отправка запроса на создание заказа в системе"):
            response = requests.post(Url.BASE_URL + Url.ORDER_URL, headers = headers, json = payload)
        assert response.status_code == 200

    @allure.title("Успешное создание заказа возвращает статус успеха")
    def test_created_order_with_token_return_status_success(self, create_user):
            ingridients = get_random_ingredients(4)
            payload = {"ingredients": ingridients}
            token = create_user['accessToken']
            headers = {'Authorization': f"{token}"}
            with allure.step("Отправка запроса на создание заказа в системе"):
                response = requests.post(Url.BASE_URL + Url.ORDER_URL, headers = headers, json = payload)
            assert response.json()['success'] 

    @allure.title("Успешное создание заказа возвращает номер заказа")
    def test_created_order_with_token_return_order_number(self, create_user):
                ingridients = get_random_ingredients(4)
                payload = {"ingredients": ingridients}
                token = create_user['accessToken']
                headers = {'Authorization': f"{token}"}
                with allure.step("Отправка запроса на создание заказа в системе"):
                    response = requests.post(Url.BASE_URL + Url.ORDER_URL, headers = headers, json = payload)
                assert response.json()['order']['number'] is not None

    @allure.title("Успешное создание заказа без авторизации")
    def test_created_order_without_token_return_status(self):
            ingridients = get_random_ingredients(4)
            payload = {"ingredients": ingridients}
            with allure.step("Отправка запроса на создание заказа в системе"):
                response = requests.post(Url.BASE_URL + Url.ORDER_URL, json = payload)
            assert response.status_code == 200

    @allure.title("Успешное создание заказа с различным числом ингридиентов")
    @pytest.mark.parametrize('count', [1,4,9])
    def test_created_order_with_ingredients_return_status(self,count):
                ingridients = get_random_ingredients(count)
                payload = {"ingredients": ingridients}
                with allure.step("Отправка запроса на создание заказа в системе"):
                    response = requests.post(Url.BASE_URL + Url.ORDER_URL, json = payload)
                assert response.status_code == 200

    @allure.title("При создании заказа без ингридиентов возвращается статус-код")
    def test_created_order_without_ingredients_return_status(self):
                payload = {"ingredients": []}
                with allure.step("Отправка запроса на создание заказа в системе"):
                    response = requests.post(Url.BASE_URL + Url.ORDER_URL, json = payload)
                assert response.status_code == 400

    @allure.title("При создании заказа без ингридиентов возвращается статус успеха")
    def test_created_order_with_token_return_status(self, create_user):
        payload = {"ingredients": []}
        token = create_user['accessToken']
        headers = {'Authorization': f"{token}"}
        with allure.step("Отправка запроса на создание заказа в системе"):
            response = requests.post(Url.BASE_URL + Url.ORDER_URL, headers = headers, json = payload)
        assert response.json()['success'] == False

    @allure.title("При создании заказа без ингридиентов возвращается сообщение об ошибке")
    def test_created_order_with_token_return_status(self, create_user):
        payload = {"ingredients": []}
        token = create_user['accessToken']
        headers = {'Authorization': f"{token}"}
        with allure.step("Отправка запроса на создание заказа в системе"):
            response = requests.post(Url.BASE_URL + Url.ORDER_URL, headers = headers, json = payload)
        assert response.json()['message'] == Message.MESSAGE_ERROR_INGREDIENTS

    @allure.title("При создании заказа с невалидным хешом ингридиента возвращается код")
    def test_created_order_with_ingredients_return_status(self):
                payload = {"ingredients": Ingridients.INGRIDIENTS_NON_EXIST}
                with allure.step("Отправка запроса на создание заказа в системе"):
                    response = requests.post(Url.BASE_URL + Url.ORDER_URL, json = payload)
                assert response.status_code == 500