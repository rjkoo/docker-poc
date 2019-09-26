from flask import request

class UserRegistrationForm(object):
    """ Used to validate each form submission. """
    def __validate_email(self):
        pass

    def __validate_firstname(self):
        pass

    def __validate_firstname(self):
        pass

    def __validate_lastname(self):
        pass

    def __validate_password(self):
        pass

    def validate_on_submit(self):
        self.__validate_email()
        self.__validate_password()
        self.__validate_firstname()
        self.__validate_lastname()
        return True
