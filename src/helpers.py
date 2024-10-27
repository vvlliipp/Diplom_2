from faker import Faker
import random
import string


class CreateUser:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def create_unique_user():
        email_prefix = CreateUser.generate_random_string(10)
        email = f"{email_prefix}@yandex.ru"
        password = CreateUser. generate_random_string(10)
        name = CreateUser. generate_random_string(10)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

    @staticmethod
    def create_register_user():
        register_user = {
            'email': 'vvlliipp@mail.ru',
            'password': '123456',
            'name': 'vvlliipp'
        }
        return register_user

    @staticmethod
    def create_user_without_email():
        fake = Faker()
        user_without_email = {
            'email': '',
            'password': fake.password(),
            'name': fake.name()
        }
        return user_without_email

    @staticmethod
    def create_user_without_password():
        fake = Faker()
        user_without_password = {
            'email': fake.email(),
            'password': '',
            'name': fake.name()
        }
        return user_without_password

    @staticmethod
    def create_user_without_name():
        fake = Faker()
        user_without_name = {
            'email': fake.email(),
            'password': fake.password(),
            'name': ''
        }
        return user_without_name


class LoginUser:
    @staticmethod
    def login_with_valid_credentials():
        return {
            'email': 'vvlliipp@mail.ru',
            'password': '123456'
        }

    @staticmethod
    def login_with_invalid_credentials():
        fake = Faker()
        return {
            'email': fake.email(),
            'password': fake.password()
        }





