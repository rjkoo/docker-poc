from flask import url_for
from lib.tests import assert_status_with_message
from app.blueprints.contact.forms import ContactForm

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

    def test_validator_form_with_bad_input(self, client):
        """ Validator should return False when bad input supplied."""
        invalid_form = {
            "email": "abc",
            "message": None
        }

        contact_form = ContactForm( invalid_form )
        assert contact_form.validate_on_submit() is False


    def test_validator_form_with_good_input(self, client):
        """ Validator should return True when good input supplied."""
        invalid_form = {
            "email": "abc@gmail.com",
            "message": "this is a message."
        }

        contact_form = ContactForm( invalid_form )
        assert contact_form.validate_on_submit() is True
