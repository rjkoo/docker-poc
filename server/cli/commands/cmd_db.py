import click
import random
from faker import Faker
from sqlalchemy_utils import database_exists, create_database

from app.app import create_app
from app.extensions import db

# Models
from app.blueprints.user.models import User
from app.blueprints.plan_of_work.models import (
        PlanOfWork,
        CriticalIssue
)

# Create an app context for the database connection
app = create_app()
db.app = app

# Create a faker instance
fake = Faker()

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

    print("Seeding users.")
    # **params converts all the dictionary pairs to keyword arguments
    return User(**params).save()


@click.command()
@click.option('--plan-count', default=3, help='Number of plans to make.')
@click.option('--issue-count', default=3, help='Number of issues per plan')
def seed_plans(plan_count, issue_count):
    """
    Seed the database with an initial Plan and Critical Issues.

    :return: User Instance
    """

    status_options = ['Draft', 'Submission in Progress', 'NIFA Review']

    for i in range(plan_count):
        plan_of_work = {
            'status': random.choice(status_options),
            'year': fake.future_date(end_date="+4y", tzinfo=None).year,
            'cohort': f"University of {fake.state()}",
            'exec_summary': fake.text(),
            'merit_peer_review': fake.text(),
            'stakeholder_actions': fake.text(),
            'stakeholder_id_methods': fake.text(),
            'stakeholder_collection_method': fake.text(),
            'stakeholder_how_considered': fake.text()
        }

        new_pow = PlanOfWork(**plan_of_work).save()

        for j in range(1, issue_count+1):
            critical_issue = {
                'term': random.choice(['short', 'intermediate', 'long']),
                'plan_id': new_pow.id,
                'order': j,
                'name': fake.sentence()
            }

            ci = CriticalIssue(**critical_issue).save()
    print("Seeding plans of work.")
    return None

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
    ctx.invoke(seed_plans)


# Add the commands to the group
cli.add_command(init)
cli.add_command(seed)
cli.add_command(seed_plans)
cli.add_command(reset)
