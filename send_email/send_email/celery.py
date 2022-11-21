import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_email.settings')

app = Celery("send_email")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
