from send_email.celery import app
from django.conf import settings
from django.core.mail import send_mail
from send.models import MailingEmail
from django.template.loader import render_to_string


@app.task
def send_email_to_subscriber(id, heading):
    mailing_email = MailingEmail.objects.get(id=id)
    topic = mailing_email.topic
    msg_text = mailing_email.text
    email = [sub.email for sub in mailing_email.subscriber.all()]
    email_from = settings.EMAIL_HOST_USER
    context = {
        'msg_text': msg_text.replace('\n', '<br>'),
        'heading': heading,
        'id': id
    }
    template = 'test_email'
    msg_html = render_to_string(f'email/{template}.html', context)
    send_mail(
        topic,
        msg_text,
        email_from,
        email,
        fail_silently=False,
        html_message=msg_html
    )
