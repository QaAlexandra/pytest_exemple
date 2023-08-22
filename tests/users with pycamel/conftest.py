from src.baseclasses.auth_token import sing_up_and_get_tocken, activate_and_get_accesse_token, get_token
from src.baseclasses.db_classes import delete_test_user_from_db, change_mail_in_db, get_refresh_token
from src.baseclasses.owncloud import delete_from_cloud
import pytest
import requests
from configuration import *
from pycamel import RouterMaker
import sys

sys.path.append('../../')



user_router_maker = RouterMaker(PORT_USERS)

users_sing_up = user_router_maker.make_router(SING_UP)
users_sing_in = user_router_maker.make_router(SING_IN)
user_activate = user_router_maker.make_router(CONFIRM)
users_get_one = user_router_maker.make_router(GET_ONE)
users_update = user_router_maker.make_router(UPDATE_USER)
users_logout = user_router_maker.make_router(LOGOUT)
users_change_password_massege = user_router_maker.make_router(PASS_MASSEGE)
users_change_password = user_router_maker.make_router(CHANGE_PASS)
users_change_mail = user_router_maker.make_router(CHANGE_EMAIL)
users_change_mail_confirm = user_router_maker.make_router(CONFIRM_MAIL)
users_update_token = user_router_maker.make_router(UPDATE_TOKEN)


@pytest.fixture()
def change_password_massege():
    return users_change_password_massege


@pytest.fixture()
def sing_up_route():
    return users_sing_up


@pytest.fixture()
def sing_in_route():
    return users_sing_in


@pytest.fixture(scope="session")
def auth_token():
    return sing_up_and_get_tocken()


@pytest.fixture()
def get_token_from_massage():
    token = get_token()
    return {'Authorization': 'Bearer ' + token}


@pytest.fixture()
def activate_user():
    return user_activate


@pytest.fixture()
def change_pass():
    return users_change_password


@pytest.fixture(scope="session")
def access_token_headers():
    response = requests.post(data=data_g, url=http + HOST + PORT_USERS + SING_IN)
    obj = response.json()
    print(obj)
    auth_token = obj["access_token"]
    print(obj)
    return {'Authorization': 'Bearer ' + auth_token}


@pytest.fixture()
def refresh_token():
    response = requests.post(data=data_g, url=http + HOST + PORT_USERS + SING_IN)
    obj = response.json()
    return obj["refresh_token"]


@pytest.fixture()
def hesders_with_wrong_token():
    return {'Authorization': 'Bearer ' + " dsadasdas"}


@pytest.fixture()
def get_one_user():
    return users_get_one


@pytest.fixture()
def update_user():
    return users_update


@pytest.fixture()
def logout_user():
    return users_logout


@pytest.fixture()
def delete_user_from_db():
    yield
    delete_test_user_from_db("pstest.qa@yandex.com")
    delete_from_cloud("pstest.qa@yandex.com")


@pytest.fixture()
def access_token_from_new_accaunt():
    return activate_and_get_accesse_token()


@pytest.fixture()
def change_password():
    return users_change_password


@pytest.fixture()
def get_activation_tocken():
    return get_token()


@pytest.fixture()
def send_email_change_massege():
    return users_change_mail


@pytest.fixture()
def change_mail():
    yield
    return change_mail_in_db(from_mail=data_ya['email'], to_mail=data_g['email'])


@pytest.fixture()
def confirm_mail():
    return users_change_mail_confirm


@pytest.fixture()
def update_token():
    return users_update_token


@pytest.fixture()
def refresh_token_from_db():
    return get_refresh_token(data_g["email"])[0]
