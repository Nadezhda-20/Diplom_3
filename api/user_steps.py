from __future__ import annotations
import allure
import requests
from models.user import User
from utils.constants import POST_REGISTER_URL, DELETE_USER_URL

class UserSteps:
    @allure.step("Создание пользователя через API")
    def create_user(self, user: User) -> requests.Response:
        response = requests.post(POST_REGISTER_URL, json={
            "email": user.email,
            "password": user.password,
            "name": user.name,
        })
        return response

    @allure.step("Извлечение accessToken из ответа API")
    def extract_access_token(self, response: requests.Response) -> str:
        data = response.json()
        return data.get("accessToken", "")

    @allure.step("Удаление пользователя через API")
    def delete_user(self, user: User) -> requests.Response:
        headers = {}
        auth_value = user.authorization_header_value()
        if auth_value:
            headers["Authorization"] = auth_value
        response = requests.delete(DELETE_USER_URL, headers=headers)
        return response
