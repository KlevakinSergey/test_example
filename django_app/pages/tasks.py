from django.core.mail import send_mail
from main.celery import app


@app.task
def send_email_contact(subject, body_mail, sender, recipient):
    send_mail(subject, body_mail, sender, recipient)
    return True
