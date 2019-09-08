from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    url_for)

from app.blueprints.contact.forms import ContactForm

contact = Blueprint('contact', __name__, template_folder='templates')

@contact.route('/contact', methods=['GET', 'POST'])
def index():

    form = ContactForm() # Create a new contact form

    if form.validate_on_submit(): # Differentiates between GET/POST request
        #from app.blueprints.contact.tasks import deliver_contact_email

        #deliver_contact_email.delay(request.form.get('email'),
        #                            request.form.get('message'))

        email = request.form['email']
        message = request.form['message']
        # Flash message
        print(f"contact.index Success. email={email} message={message}")

        # flash("Thanks, we'll be in touch shortly.", 'success')
        return "form sucessfully submitted"

    return "/contact"
