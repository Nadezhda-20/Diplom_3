import json
import logging
import random
import string
import time
import uuid

import allure
import requests

from data import Endpoints, Urls


class Request:
    @staticmethod
    @allure.step("POST request.")
    def post(path, payload, access_token=""):
        return requests.post(
            Urls.URL_SERVICE + path,
            headers=Funcs.auth_header(access_token),
            data=json.dumps(payload),
            timeout=10,
        )

    @staticmethod
    @allure.step("DELETE request.")
    def delete(path, access_token=""):
        return requests.delete(
            Urls.URL_SERVICE + path,
            headers=Funcs.auth_header(access_token),
            timeout=10,
        )

    @staticmethod
    @allure.step("GET request.")
    def get(path, access_token=""):
        return requests.get(
            Urls.URL_SERVICE + path,
            headers=Funcs.auth_header(access_token),
            timeout=10,
        )


class User:
    @staticmethod
    @allure.step("Регистрация пользователя (API) и возврат данных.")
    def register():
        user = Generator.get_user_payload()
        response = Request.post(Endpoints.USER_REGISTER, user, "")

        if response.status_code != 200:
            raise AssertionError(f"Пользователь не создан: {response.status_code}, {response.text}")

        Funcs.message("Пользователь создан")
        resp = response.json()        
        resp["user"]["password"] = user.get("password")
        return resp

    @staticmethod
    @allure.step("Удаление пользователя (API).")
    def delete(access_token):
        response = Request.delete(Endpoints.USER, access_token)
        if response.status_code != 202:
            raise AssertionError(f"Пользователь не удален: {response.status_code}, {response.text}")
        Funcs.message("Пользователь удален")


class Order:
    @staticmethod
    @allure.step("Получение ингредиентов (API).")
    def get_ingredients():
        response = Request.get(Endpoints.INGREDIENTS, "")
        if response.status_code != 200:
            raise AssertionError(f"Список ингредиентов не получен: {response.status_code}, {response.text}")
        Funcs.message("Список ингредиентов получен")
        return response.json()

    @staticmethod
    @allure.step("Создание списка ингредиентов с сортировкой по типу.")
    def sorted_ingredients():
        ingredients = Order.get_ingredients()
        sorted_ings = {"buns": [], "fillings": [], "sauces": []}

        for ing in ingredients.get("data", []):
            if ing.get("type") == "bun":
                sorted_ings["buns"].append(ing)
            elif ing.get("type") == "sauce":
                sorted_ings["sauces"].append(ing)
            elif ing.get("type") == "main":
                sorted_ings["fillings"].append(ing)

        return sorted_ings

    @staticmethod
    @allure.step("Создание набора ингредиентов для заказа.")
    def make_burger():
        ings_list = Order.sorted_ingredients()
        bun = random.choice(ings_list["buns"])
        sauce = random.choice(ings_list["sauces"])
        filling = random.choice(ings_list["fillings"])
    
        ingredients = [bun["_id"], bun["_id"], sauce["_id"], filling["_id"]]
        return {"ingredients": ingredients}

    @staticmethod
    @allure.step("Создание заказа (API) и получение номера.")
    def submit_order(user):
        payload = Order.make_burger()
        token = user.get("accessToken", "")
        response = Request.post(Endpoints.ORDER, payload, token)
        if response.status_code != 200:
            raise AssertionError(f"Заказ не создан: {response.status_code}, {response.text}")
        Funcs.message("Заказ создан")
        return str(response.json()["order"]["number"])


class Generator:
    @staticmethod
    @allure.step("Генерация уникальных данных пользователя (без Faker).")
    def get_user_payload():
        uniq = uuid.uuid4().hex[:10]
        email = f"ui_test_{uniq}@example.com"        
        password = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        name = ("user" + str(int(time.time())))[-8:].capitalize()
        return {"email": email, "password": password, "name": name}


class Funcs:
    @staticmethod
    def message(message):
        allure.attach("", message, attachment_type=allure.attachment_type.TEXT)
        logging.info(message)

    @staticmethod
    @allure.step("Создание headers с токеном авторизации.")
    def auth_header(token):
        return {
            "Content-Type": "application/json",
            "Authorization": f"{token}",
        }
