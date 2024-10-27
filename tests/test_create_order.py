import pytest
import allure
import requests
from src.data import Url, Answer, IdIngredients


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized_with_ingredients(self, create_and_delete_user):
        user = create_and_delete_user
        response_user = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", data=user)
        token = response_user.json()['accessToken']
        headers = {"Authorization": f'{token}'}
        payload = {'ingredients': [IdIngredients.Bun_1, IdIngredients.Sauce]}
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_ORDERS}",
                                 headers=headers,
                                 data=payload)
        assert response.json().get('success') is True

    @allure.title("Создание заказа с авторизацией без ингредиентов")
    def test_create_order_authorized_without_ingredients(self, create_and_delete_user):
        user = create_and_delete_user
        response_user = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", data=user)
        token = response_user.json()['accessToken']
        headers = {"Authorization": f'{token}'}
        payload = {'ingredients': []}
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_ORDERS}",
                                 headers=headers,
                                 data=payload)
        assert response.status_code == 400 and Answer.answer_no_ingredients in response.text

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self):
        payload = {'ingredients':[IdIngredients.Bun_1, IdIngredients.Sauce]}
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_ORDERS}", data=payload)
        assert response.json().get('success') is True

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, create_and_delete_user):
        user = create_and_delete_user
        response_user = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", data=user)
        token = response_user.json()['accessToken']
        headers = {"Authorization": f'{token}'}
        payload = {'ingredients': [IdIngredients.Bun_2, IdIngredients.Sauce_2]}
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_ORDERS}",
                                 headers=headers,
                                 data=payload)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
