import click
from sqlalchemy_utils import database_exists, create_database

from app.app import create_app
from app.extensions import db
from app.blueprints.user.models import User

# Create an app context for the database connection
app = create_app()
db.app = app

# Group decorator allows me to create a command with sub commands.
@click.group()
def cli():
    """ Run PostreSQL related tasks."""
    pass

# Option decorator attaches an option to the command.
@click.command()
@click.option('--with-testdb/--no-with-testdb', default=False,
              help='Create a test db too?')
def init(with_testdb):
    """
    Initialize the database.

    :param with_testdb: Create a database test database
    :return: None
    """
    db.drop_all() # Drops all the tables
    db.create_all() # Creates all the tables from Models

    if with_testdb:
        db_uri = f"{app.config['SQLALCHEMY_DATABASE_URI']}_test"

       # Check if the provided database name exists
        if not database_exists(db_uri):
            # If it doesn't exist, create the database
            create_database(db_uri)

    return None


@click.command()
def seed():
    """
    Seed the database with an initial user.

    :return: User Instance
    """
    # Look for the user with the seed admin email first. If the user
    # already exists in the database, exit the function
    if User.find_by_identity(app.config['SEED_ADMIN_EMAIL']) is not None:
        return None

    # Otherwise Create and Insert the user
    params = {
        'role': 'admin',
        'email': app.config['SEED_ADMIN_EMAIL'],
        'password': app.config['SEED_ADMIN_PASSWORD']
    }

    # **params converts all the dictionary pairs to keyword arguments
    return User(**params).save()


@click.command()
@click.option('--with-testdb/--no-with-testdb', default=False,
              help='Create a test db too?')
# Context is special internal object that holds state relevate for the script
# execution at every single level. Can pass internal objects around and do things
# like reading from environment variables.
@click.pass_context
def reset(ctx, with_testdb):
    """
    Init and seed automatically.

    :param with_testdb: Create a test database
    :return: None
    """
    # Basically issues other commands using the 
    # the context that is ctx. Lets us call one command from another command.
    ctx.invoke(init, with_testdb=with_testdb) # In this case, the first argument
                                              # is a callback and the keyword
                                              # arguments are forwarded directly
                                              # to the init function.
    ctx.invoke(seed) # In this case, invoke is passed a Click command function

# Add the commands to the group
cli.add_command(init)
cli.add_command(seed)
cli.add_command(reset)
