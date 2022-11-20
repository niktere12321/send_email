from django import forms
from django.contrib.auth import get_user_model

from .models import Subscriber

User = get_user_model()


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email', 'birthday', 'first_name', 'last_name']