import re
from flask import escape

class ContactForm(object):
    # Contact Form
    #   Email - Sender's email address
    #   Message - Message from the sender

    def __init__(self, form):
        """
        :param form: Request.form
        """
        self._email = form.get('email')
        self._message = form.get('message')
        self._errors = []

    def _validate_email(self):
        """
        Validate email address against a Regex pattern.

        :return: Boolean
        """
        match = re.match(
            '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
            self._email)

        if match == None:
            self._errors.append("Invalid Email")
            print("location=forms.py action=validate_email error='bad email'")
            return False
        else:
            return True


    def _validate_message(self):
        """
        Validate user message field of form.

        :return: Boolean
        """

        if self._message == "" or self._message == None: # empty message
            self._errors.append("Invalid message.")
            print("location=contact.forms.py action=validate_message error='bad message'")
            return False
        else:
            self._message = escape(self._message)
            return True


    def validate_on_submit(self):
        """
        Calls each of the form validators of the form _validate_SOME_ITEM, and
        determines if any returned false.

        :return: Boolean
        """
        validator_results = [
                getattr(self, attr)() # Execute each validator
                for attr in dir(self) 
                if '_validate_' in attr]
        return False not in validator_results


    def get_validated_email(self):
        return self._email


    def get_validated_message(self):
        return self._message


    def get_errors(self):
        return {"Submission Errors": self._errors}
