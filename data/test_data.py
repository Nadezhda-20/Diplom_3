from __future__ import annotations
import random
import string

def _rand_alnum(n: int) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(n))

def generate_user_data():    
    name = _rand_alnum(10)
    email = f"{_rand_alnum(7)}@example.com"
    correct_password = _rand_alnum(6) 
    wrong_password = _rand_alnum(5)   
    return name, email, correct_password, wrong_password


def generate_api_user_data():
    name = _rand_alnum(6)
    email = f"{_rand_alnum(7)}@yandex.ru"
    password = _rand_alnum(8)
    return name, email, password
