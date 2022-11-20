from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from subscriber.models import Subscriber
from .models import MailingEmail

User = get_user_model()


class MailingEmailForm(forms.ModelForm):
    heading = forms.CharField(
        widget=forms.TextInput(),
        label='Заголовок письма',
        required=False
    )
    pending_mailing = forms.BooleanField(
        required=False,
        label='Отложеное письмо'
    )
    pending_mailing_date = forms.DateField(
        widget=forms.SelectDateWidget(),
        label='Дата',
        required=False,
    )
    pending_mailing_time = forms.TimeField(
        widget=forms.TimeInput(),
        label='Время',
        required=False
    )

    class Meta:
        model = MailingEmail
        fields = ('topic', 'text', 'subscriber')
        labels = {'subscriber': _('Подписчики'),}
        help_texts = {'text': "Для использования переменных",}
        widgets = {
            'topic': forms.TextInput(attrs={'type': 'text'}),
            'text': forms.Textarea(attrs={'type': 'text'}),
            'subscriber': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        super(MailingEmailForm, self).__init__(*args,**kwargs)
        self.fields['subscriber'].queryset = Subscriber.objects.filter(user=self.author)
