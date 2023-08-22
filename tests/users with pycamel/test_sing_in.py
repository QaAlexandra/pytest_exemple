import pytest
from src.schemas.user import UserPassError, ShortAnswer, UserError
from src.enums.user_enums import ErorsMessege
from configuration import *


def test_users_sing_in_succsess(sing_in_route):
    """Успешная авторизация 201"""
    response = sing_in_route.post(json=data_g)
    response.assert_status_code([201]).validate(ShortAnswer)


def test_sing_in_with_non_activated_accaunt(sing_in_route, sing_up_route, delete_user_from_db):
    """авторизоваться с не активным акаунтом 403"""
    sing_up_route.post(json=data_ya)
    response = sing_in_route.post(json=data_ya)
    response.assert_status_code([403]). \
        validate(UserError). \
        assert_parameter('message', ErorsMessege.USER_NON_ACTIVATE)



@pytest.mark.parametrize("email, password", [
        (data_g['email'], "11111"),
        (data_g['email'], ""),
        ("email", data_g['password']),
        ("", data_g['password']),
        ("", ""),
        ("11111", "11111")])
def test_users_sing_in_with_wrong_credentials(sing_in_route, email, password):
    """Авторизация с неверным паролем 401"""
    response = sing_in_route.post(json={
        'email': email,
        'password': password
    })
    response.assert_status_code([401]).validate(UserPassError)
    print(response.get_response_json())



def test_sing_in_empty(sing_in_route):
    """Авторизация неверный email 401"""
    response = sing_in_route.post(json={})
    response.assert_status_code([201])
