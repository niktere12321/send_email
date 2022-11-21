from send_email.celery import app
from django.conf import settings
from django.core.mail import send_mail
from send.models import MailingEmail
from django.template.loader import render_to_string


@app.task
def send_email_to_subscriber(id, heading):
    """Отправка на почту"""
    mailing_email = MailingEmail.objects.get(id=id)
    topic = mailing_email.topic
    msg_text = mailing_email.text
    email_from = settings.EMAIL_HOST_USER
    for sub in mailing_email.subscriber.all():
        email = [sub.email]
        message = msg_text
        heading_sub = heading
        message = message.replace('!name', sub.first_name)
        message = message.replace('!last_name', sub.last_name)
        message = message.replace('!birthday', str(sub.birthday))
        heading_sub = heading_sub.replace('!name', sub.first_name)
        heading_sub = heading_sub.replace('!last_name', sub.last_name)
        heading_sub = heading_sub.replace('!birthday', str(sub.birthday))
        context = {
            'topic': topic,
            'heading': heading_sub,
            'msg_text': message.replace('\n', '<br>'),
            'author': f'{mailing_email.author.first_name} \
                {mailing_email.author.last_name}',
            'id': id,
            'id_sub': sub.pk
        }
        msg_html = render_to_string(f'email/email.html', context)
        send_mail(
            topic,  
            message,
            email_from,
            email,
            fail_silently=False,
            html_message=msg_html
        )
