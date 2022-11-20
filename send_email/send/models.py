from django.contrib.auth import get_user_model
from django.db import models
from subscriber.models import Subscriber

User = get_user_model()


class MailingEmail(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.TextField('Тема письма')
    text = models.TextField('Текст письма')
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)
    subscriber = models.ManyToManyField(Subscriber)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рассылка письма'
        verbose_name_plural = 'Рассылки писем'

    def __str__(self):
        return self.text[:15]
