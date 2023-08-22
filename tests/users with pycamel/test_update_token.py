from src.schemas.user import ShortAnswer, UserError


class TestUpdateToken:

    def test_update_success(self, update_token, refresh_token_from_db):
        """Update token"""
        print(refresh_token_from_db)
        response = update_token.set_filters({"refresh_token": refresh_token_from_db}).put()
        response.assert_status_code([200]).validate(ShortAnswer)

    def test_update_without_token(self, update_token):
        """Update token without token"""
        response = update_token.put()
        response.assert_status_code([401]).validate(UserError)
