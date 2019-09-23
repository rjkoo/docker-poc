from app.app import create_celery_app
from lib.flask_mailplus import send_template_message

celery = create_celery_app()

@celery.task()
def deliver_contact_email(email, message):
    """
    Send a contact e-mail.
    :param email: E-mail address of the visitor
    :type: email: str

    :param message: Email message
    :type: str

    :return none
    """

    context = {'email': email, 'message': message}

    send_template_message(subject='[FlashCard App] Contact',
                          sender=email,
                          recipients=[celery.conf.get('MAIL_USERNAME')],
                          reply_to=email,
                          template='contact/mail/contact_message', ctx=context)

    return None
