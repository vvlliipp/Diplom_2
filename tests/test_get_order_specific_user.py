import pytest
import allure
import requests
from src.data import Url, Answer

@allure.suite("Получение заказов пользователя")
class TestGetUserOrders:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_authorized_user(self, create_and_delete_user):
        user = create_and_delete_user
        response_user = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", data=user)
        token = response_user.json()['accessToken']
        headers = {"Authorization": f'{token}'}
        response = requests.get(f"{Url.STELLAR_BURGER}{Url.GET_ORDER_SPECIFIC_USER}", headers=headers)
        assert response.json().get('success') is True


    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_unauthorized_user(self):
        response = requests.get(f"{Url.STELLAR_BURGER}{Url.GET_ORDER_SPECIFIC_USER}")
        assert response.status_code == 401 and Answer.answer_no_autorization_get_order in response.text

