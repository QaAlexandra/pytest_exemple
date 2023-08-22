from src.schemas.user import UserFullAnswer, UserError
from src.enums.user_enums import  ErorsMessege


def test_get_one_success(get_one_user, access_token_headers):
    """get one user success"""

    resp = get_one_user.set_headers(access_token_headers).get()
    print(resp.get_response_json())
    obj = resp.assert_status_code([200]).validate(UserFullAnswer)



def test_get_one_without_token(get_one_user):
    """get one user without token"""

    resp = get_one_user.get()
    resp.assert_status_code([401]).validate(UserError).assert_parameter("message", ErorsMessege.NO_TOKEN)\


def test_get_one_with_invalid_token(get_one_user, hesders_with_wrong_token):
    """get one user with invalid token 412"""

    resp = get_one_user.set_headers(hesders_with_wrong_token).get()
    resp.assert_status_code([412]).validate(UserError).assert_parameter("message", ErorsMessege.INVALID_TOKEN)

