from app.extensions import mail
from app.blueprints.contact.tasks import deliver_contact_email

class TestTasks(object):
    def test_deliver_contact_form_email(self):
        """ Deliver contact email."""
        form = {
            'email': 'test@test.com',
            'message': 'Test message from application.'
        }

        with mail.record_messages() as outbox:
            deliver_contact_email(form.get('email'), form.get('message'))

            assert len(outbox) == 1
            assert form.get('email') in outbox[0].body
