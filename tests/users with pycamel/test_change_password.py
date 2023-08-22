from src.schemas.user import UserError, UserFullAnswer, UserPassError
from configuration import *


class TestChangePassword:
    """Test Change Password"""

    def test_change_pass_massage_success(self, change_password_massege):
        """Activation massage 200"""

        response = change_password_massege.set_filters({"email": data_ya["email"]}).get()
        print(response.get_response_json())
        response.assert_status_code([200]).validate(UserFullAnswer)

    def test_change_not_exist_email(self, change_password_massege):
        """Activation massage sent to nonexistent email"""

        response = change_password_massege.set_filters({'email': "mail@mail.com"}).get()
        response.assert_status_code([404]).validate(UserError)

    def test_user_confirm_password(self, change_pass, get_token_from_massage):
        """Comfirm password"""
        resp = change_pass.set_headers(get_token_from_massage) \
            .put(json={"password": data_ya['password']})
        resp.assert_status_code([200]).validate(UserFullAnswer)

    #встроить faiker
    #Проверить с коварными строками
    def test_send_short_password(self,  change_pass,get_token_from_massage):
        """Change password to invalid password 401"""
        resp = change_pass.set_headers(get_token_from_massage) \
            .put(json={"password": "111"})
        resp.assert_status_code([401]).validate(UserPassError)

    def test_use_token_again(self, change_pass, get_token_from_massage):
        """Use token again"""
        response = change_pass.set_headers(get_token_from_massage) \
            .put(json={"password": data_ya['password']})
        response.assert_status_code([409]).validate(UserError)

    def test_change_pass_with_no_token(self, change_pass):
        """Change password with no token"""
        resp = change_pass.set_headers({'Authorization': 'Bearer ' + ''}).put(json={"password":data_g["password"]})
        resp.assert_status_code([412]).validate(UserError)

    def test_activate_token_nonvalid(self, change_pass, delete_user_from_db):
        """Change password with invalid token"""
        response = change_pass.set_headers({'Authorization': 'Bearer ' + 'aaaaaa'}) \
            .put(json={"password":data_g["password"]})
        response.assert_status_code([412]).validate(UserError)

