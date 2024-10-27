import pytest
import requests
from src.data import Url
from src.helpers import CreateUser


@pytest.fixture
def create_and_delete_user():
    user = CreateUser.create_unique_user()
    yield user
    response = requests.post(f'{Url.STELLAR_BURGER}{Url.LOGIN_USER}', data=user)
    token = response.json()['accessToken']
    requests.delete(f'{Url.STELLAR_BURGER}{Url.CHANGE_DATA_USER}', headers={'Authorization': token})
