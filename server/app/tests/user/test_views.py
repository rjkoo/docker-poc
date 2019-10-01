from flask import url_for
from lib.tests import assert_status_with_message

class TestUser(object):
    def test_user_registration_form(self, client):
        """ User registration form should respond with a success 200 when all
            fields are present and valid."""
        form = {
            'email': "test@test.com",
            'first_name': "first",
            'last_name': "last",
            'password': "letmein123"
        }

        response = client.post(url_for('user.register'), data = form,
                               follow_redirects=True)
        assert_status_with_message(200,
                                   response, 'Submitted. Thank you.')
