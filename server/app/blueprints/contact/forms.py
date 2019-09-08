
class ContactForm(object):
    # Contact Form
    #   Email - Sender's email address
    #   Message - Message from the sender

    def __validate_email(self):
        pass

    def __validate_message(self):
        pass

    def validate_on_submit(self):
        self.__validate_email()
        self.__validate_message()
        return True
