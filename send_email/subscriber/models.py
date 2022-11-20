from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    birthday = models.DateField()
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')

    class Meta:
        ordering = ('birthday',)
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return self.first_name
