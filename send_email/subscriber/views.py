from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import SubscriberForm
from .models import Subscriber

User = get_user_model()


@login_required
def index(request):
    """Просмотр всех подписчиков"""
    context = {
        'all_subscriber': Subscriber.objects.filter(user=request.user),
    }
    return render(request, 'subscriber/index.html', context)


@login_required
def create(request):
    """Создание подписчика"""
    form = SubscriberForm(request.POST or None)
    if request.POST and form.is_valid():
        subscriber = form.save(commit=False)
        subscriber.user = request.user
        subscriber.save()
        return redirect(reverse('subscriber:index'))
    context = {'form': form}
    return render(request, 'subscriber/create.html', context)


@login_required
def edit(request, id):
    """Редактирование подписчика"""
    subscriber = get_object_or_404(Subscriber, pk=id)
    form = SubscriberForm(
        request.POST or None,
        files=request.FILES or None,
        instance=subscriber
    )
    if request.POST and form.is_valid():
        layout = form.save(commit=False)
        layout.author = request.user
        layout.save()
        return redirect(reverse('subscriber:index'))
    context = {'form': form}
    return render(request, 'subscriber/edit.html', context)
