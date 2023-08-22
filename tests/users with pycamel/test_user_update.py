from src.schemas.user import UserFullAnswer, UserError, UpdatedUser
from src.enums.user_enums import ErorsMessege, UserErrorsMSG


def test_user_update_success(access_token_from_new_accaunt, delete_user_from_db, update_user):
    """Check update func"""

    body = {
        "is_superuser": True,
        "is_staff": False,
        "data": {
            "погода": "всякая",
            "массив": ["значений, разных"]
        }
    }

    response = update_user.set_headers(access_token_from_new_accaunt).put(json=body)
    response.assert_status_code([200]). \
        validate(UpdatedUser). \
        assert_parameter('массив', ['значений, разных'])


def test_update_with_new_feelds(access_token_headers, update_user):
    """Update with new fields 200 """
    body = {
        "is_supe": True,
        "is": False,
        "d": {
            "погода": "не такая",

        }
    }

    response = update_user.set_headers(access_token_headers).put(json=body)
    response.assert_status_code([200]).validate(UserFullAnswer)


def test_user_update_without_token(update_user):
    """Update without token 401"""
    response = update_user.put(). \
        assert_status_code([401]). \
        validate(UserError). \
        assert_parameter('message', ErorsMessege.NO_TOKEN)
    obj = response.get_response_json()
    print(obj)


def test_update_with_invalid_token(update_user, hesders_with_wrong_token):
    """Update with invalid token 412"""
    body = {
        "is_super": True,
        "is": False,
        "data": {
            "field1": "value",
            "field2": ["value1, value2"]
        }
    }
    response = update_user. \
        set_headers(hesders_with_wrong_token). \
        put(json=body). \
        assert_status_code([412]). \
        validate(UserError). \
        assert_parameter('message', ErorsMessege.INVALID_TOKEN)
    print(response)
