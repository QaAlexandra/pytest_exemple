from src.enums.user_enums import ErorsMessege
from src.schemas.user import UserFullAnswer, UserError


def test_logout_sucsses(access_token_headers, logout_user, refresh_token):
    """logout"""
    response = logout_user.set_filters({"refresh_token": refresh_token}).put()
    obj = response.assert_status_code([200]). \
        validate(UserFullAnswer)
    print(obj)


def test_user_logout_without_token(logout_user):
    """logout without token"""
    logout_user.put(). \
        assert_status_code([401]). \
        validate(UserError). \
        assert_parameter('message', ErorsMessege.NO_TOKEN)


def test_logout_with_invalid_token(logout_user, hesders_with_wrong_token):
    """logout with invalid token"""
    response = logout_user.set_filters({"refresh_token": " xMTA5M30.71o5xq4i4PrRpSiKmxNR"}).put().assert_status_code(
        [412])
    response.assert_status_code([412]). \
        validate(UserError). \
        assert_parameter('message', ErorsMessege.INVALID_TOKEN)
    obj = response
    print(obj)
