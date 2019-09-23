from flask import url_for
from lib.tests import assert_status_with_message

class TestContact(object):
    def test_contact_form(self, client):
        """ Contact form should redierect with a message."""
        form = {
            "email": "test@test.com",
            "message": "Test message from flashcard app."
        }

        response = client.post(url_for('contact.index'), data=form,
                                follow_redirects=True)
        assert_status_with_message(200, response, 'form sucessfully submitted')
