from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from celery_task.task import send_email_to_subscriber
from datetime import datetime
from .forms import MailingEmailForm
from .models import MailingEmail

User = get_user_model()


@login_required
def index(request):
    """Просмотр всех созданных рассылок"""
    context = {
        'all_mailing_email': MailingEmail.objects.filter(author=request.user),
    }
    return render(request, 'send/index.html', context)


@login_required
def create_mailing(request):
    """Создание рассылки"""
    form = MailingEmailForm(request.POST or None, author=request.user)
    if request.POST and form.is_valid():
        mailing = form.save(commit=False)
        mailing.author = request.user
        subscriber_query_list = form.cleaned_data['subscriber']
        mailing.save()
        mailing.subscriber.set(subscriber_query_list)
        if form.cleaned_data['pending_mailing'] is True:
            date = form.cleaned_data['pending_mailing_date']
            time = form.cleaned_data['pending_mailing_time']
            pending_mailing_datetime = datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=time.hour,
                minute=time.minute
            )
            send_email_to_subscriber.apply_async((
                    mailing.pk,
                    form.cleaned_data['heading'],
                ),
                eta=pending_mailing_datetime
            )
        else:
            send_email_to_subscriber.delay(
                mailing.pk,
                form.cleaned_data['heading'],
            )
        return redirect(reverse('send:index'))
    context = {'form': form}
    return render(request, 'send/create_mailing.html', context)


@login_required
def get_mailing(request, id):
    """Просмотр текста письма и подписчиков"""
    mailing = get_object_or_404(MailingEmail, pk=id)
    context = {'mailing': mailing, 'subscriber': mailing.subscriber.all()}
    return render(request, 'send/get_mailing.html', context)