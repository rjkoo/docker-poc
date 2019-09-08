from app.app import create_celery_app


celery = create_celery_app()

@celery.task()
def deliver_contact_email(email, message):
    pass
