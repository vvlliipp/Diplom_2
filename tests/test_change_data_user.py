import pytest
import allure
import requests
from src.data import Url, Answer
from src.helpers import CreateUser



@allure.suite("Изменение данных пользователя")
class TestChangeDataUser:
    @allure.title('Обновление данных авторизованного пользователя')
    @pytest.mark.parametrize('change_data_user', [
        ({'email': CreateUser.generate_random_string(8) + '@yandex.ru'}),
        ({'password': CreateUser.generate_random_string(10)}),
        ({'name': CreateUser.generate_random_string(10)})
    ])
    def test_change_authorized_user(self, change_data_user, create_and_delete_user):
        change_data_user = create_and_delete_user
        response_user = requests.post(f"{Url.STELLAR_BURGER}{Url.CREATE_USER}", data=change_data_user)
        token = response_user.json()['accessToken']
        headers = {"Authorization": f'{token}'}
        change_data_response = requests.patch(f"{Url.STELLAR_BURGER}{Url.CHANGE_DATA_USER}",
                                              data=change_data_user, headers=headers)
        assert change_data_response.json()['success'] is True


    @allure.title("Обновление данных неавторизованного пользователем")
    def test_update_user_unauthorized(self):
        new_email = f"{CreateUser.generate_random_string(8)}@yandex.ru"
        payload = {"email": new_email}
        response = requests.patch(f"{Url.STELLAR_BURGER}{Url.CHANGE_DATA_USER}", json=payload)
        assert response.status_code == 401 and Answer.answer_no_autorization_change_data in response.text
