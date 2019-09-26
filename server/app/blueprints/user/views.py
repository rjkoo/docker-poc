from flask import(
    Blueprint,
    request,
    url_for
)
from app.blueprints.user.forms import UserRegistrationForm
user = Blueprint('user', __name__)

@user.route('/user/register', methods=['POST'])
def register():

    if UserRegistrationForm.validate_on_submit(
        request.form):
        # Validation placeholder
        return "Submitted. Thank you."
    else:
        return "Form Error."
