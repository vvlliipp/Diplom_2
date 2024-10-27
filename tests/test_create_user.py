import pytest
import allure
import requests
from src.data import Url, Answer
from src.helpers import CreateUser


@allure.suite("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_user(self, create_and_delete_user):
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", json=create_and_delete_user)
        response_data = response.json()
        assert response_data['success'] is True

    @allure.title("Создание пользователя который уже зарегистрирован")
    def test_create_register_user(self):
        register_user = CreateUser.create_register_user()
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", json=register_user)
        assert response.status_code == 403 and Answer.answer_user_exists in response.text

    @allure.title("Создание пользователя без email")
    def test_create_user_without_email(self):
        create_user = CreateUser.create_user_without_email()
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", json=create_user)
        assert response.status_code == 403 and Answer.answer_user_no_email_or_password_or_name in response.text

    @allure.title("Создание пользователя без name")
    def test_create_user_without_name(self):
        create_user_without_name = CreateUser.create_user_without_name()
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", json=create_user_without_name)
        assert response.status_code == 403 and Answer.answer_user_no_email_or_password_or_name in response.text

    @allure.title("Создание пользователя без password")
    def test_create_user_without_password(self):
        create_user_without_password = CreateUser.create_user_without_password()
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", json=create_user_without_password)
        assert response.status_code == 403 and Answer.answer_user_no_email_or_password_or_name in response.text
