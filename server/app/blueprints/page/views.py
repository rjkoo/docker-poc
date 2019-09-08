from flask import Blueprint

page = Blueprint('page', __name__)

@page.route('/page')
def home():
    return "Hello from the home page."
