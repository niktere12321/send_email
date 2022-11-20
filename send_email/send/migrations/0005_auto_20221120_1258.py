# Generated by Django 2.2.28 on 2022-11-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0004_mailingemail_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingemail',
            name='subscriber',
            field=models.ManyToManyField(related_name='Подписчики', to='subscriber.Subscriber'),
        ),
        migrations.AlterField(
            model_name='mailingemail',
            name='text',
            field=models.TextField(verbose_name='Текст письма'),
        ),
    ]