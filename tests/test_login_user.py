import pytest
import allure
import requests
from src.data import Url, Answer
from src.helpers import LoginUser


@allure.suite("Логин пользователя")
class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    def test_login_user(self):
        login_user = LoginUser.login_with_valid_credentials()
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.LOGIN_USER}", json=login_user)
        response_data = response.json()
        assert response_data['success'] is True

    @allure.title("Логин с неверным логином")
    def test_invalid_login_user(self):
        login_user_invalid_login = LoginUser.login_with_invalid_credentials()
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.LOGIN_USER}", json=login_user_invalid_login)
        assert response.status_code == 401 and Answer.answer_login_invalid_login_password in response.text

    @allure.title("Логин с неверным паролем")
    def test_invalid_user_password(self):
        login_user_invalid_password = LoginUser.login_with_invalid_credentials()
        response = requests.post(f"{Url.STELLAR_BURGER}{Url.LOGIN_USER}", json=login_user_invalid_password)
        assert response.status_code == 401 and Answer.answer_login_invalid_login_password in response.text


