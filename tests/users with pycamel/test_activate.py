from configuration import *
from src.enums.user_enums import ErorsMessege
from src.schemas.user import ShortAnswer, UserError


class TestActivatePossitive:
    """Tests activation"""

    def test_users_activate_success(self, get_token_from_massage, activate_user, sing_up_route):
        """Normal activation 200"""
        sing_up_route.post(json=data_ya)
        response = activate_user.set_headers(get_token_from_massage) \
            .put()
        response.assert_status_code([200]).validate(ShortAnswer)

    def test_user_already_activate(self, auth_token, activate_user, get_activation_tocken, delete_user_from_db):
        """User already activate 409"""
        token = auth_token
        activate_user.set_headers(token) \
            .put().assert_status_code([409]).validate(UserError)

    def test_token_is_invalid(self, activate_user):
        """Activate with wrong token 412"""
        response = activate_user.set_headers({'Authorization': 'Bearer ' + "aaaaaa"}).put()
        response.assert_status_code([412]).validate(UserError). \
            assert_parameter("message", ErorsMessege.INVALID_TOKEN)

    def test_no_token(self, activate_user):
        """Activate without token 401"""

        response = activate_user.put()
        response.assert_status_code([401]).validate(UserError). \
            assert_parameter("message", ErorsMessege.NO_TOKEN)
