import pytest
from src.schemas.user import UserFullAnswer, UserError, WrongCredentials
from configuration import *
import sys

sys.path.append('../')
class TestUsersAuthPossitive():

    def test_users_sing_up_succsess(self, sing_up_route, delete_user_from_db):
        """Successful registration 201"""
        response = sing_up_route.post(json=data_ya)
        obj = response. \
            assert_status_code([201]). \
            validate(UserFullAnswer).get_response_json()
        print(obj)

    def test_user_sing_up_already_exist(self, sing_up_route):
        """User already registered  409"""

        response = sing_up_route.post(json=data_g)
        resp = response. \
            assert_status_code([409]). \
            validate(UserError)
        print(resp)


@pytest.mark.parametrize("email, password", [
        (data_g['email'], "11111"),
        (data_g['email'], ""),
        ("email", data_g['password']),
        ("", data_g['password']),
        ("", ""),
        ("11111", "11111")])
def test_users_sing_with_wrong_credetials(self, sing_up_route, email, password):
        """registration with wrong token 401"""
        response =sing_up_route.post(json={
            "email": email,
            "password": password
    })
        response.assert_status_code([401]).validate(WrongCredentials)




