import time

from configuration import *
from src.schemas.user import *

import sys

sys.path.append('../../')


class TestChangeMailMassege:

    def test_change_mail_massege(self, access_token_headers, send_email_change_massege):
        """email change massege sent"""
        response = send_email_change_massege.set_headers(access_token_headers). \
            set_filters({'email': data_ya["email"]}).get()
        response.assert_status_code([200])

    def test_change_mail_already_exist(self, access_token_headers, send_email_change_massege):
        """changeMail already exist"""
        response = send_email_change_massege.set_headers(access_token_headers). \
            set_filters({'email': data_g["email"]}).get()
        response.assert_status_code([409]).validate(UserError)

    def test_invalid_email(self, send_email_change_massege, access_token_headers):
        """change mail invalid email"""
        response = send_email_change_massege.set_headers(access_token_headers). \
            set_filters({'email': "dmfcopwe,cwp"}).get()
        print(response.get_response_json())
        response.assert_status_code([401]).validate(UserPassError)

    def test_send_without_token(self, send_email_change_massege):
        """change mail without token 401"""
        response = send_email_change_massege.set_filters({'email': data_ya["email"]}).get()
        response.assert_status_code([401]).validate(UserError)


class TestChangeMail:
    """change mail conformation"""

    def test_mail_been_changed(self, confirm_mail, get_token_from_massage):
        """confirm email 200"""
        token = get_token_from_massage
        time.sleep(10)
        response = confirm_mail.set_headers(token).put()
        response.assert_status_code([200]).validate(UserFullAnswer)

    def test_use_token_again(self, confirm_mail, get_token_from_massage):
        """use token again 409"""
        response = confirm_mail.set_headers(get_token_from_massage).put()
        response.assert_status_code([409]).validate(UserError)

    def test_auth_after_change_mail(self, sing_in_route, change_mail):
        """auth token after change mail 201"""
        resource = sing_in_route.post(json=data_ya)
        resource.assert_status_code([201]).validate(ShortAnswer)

    def test_no_token(self, confirm_mail):
        """confirm email without token 401"""
        response = confirm_mail.put()
        response.assert_status_code([401]).validate(UserError)

    def test_non_valid_token(self, confirm_mail):
        """confirm email with invalid token 412"""
        response = confirm_mail.set_headers({'Authorization': 'Bearer ' + 'aaaaaa'}).put()
        response.assert_status_code([412]).validate(UserError)
