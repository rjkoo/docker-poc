import pytest

from app.app import create_app

@pytest.yield_fixture(scope='session')
def app():
    """
    Setup a flask test app; Executes only once.
    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
        'SERVER_NAME': 'localhost:8000'
    }

    _app = create_app(settings_override=params)

    # Setup app context before running tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client; Executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()



