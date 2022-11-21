from rest_framework.response import Response
from django.http import HttpResponse
import telegram
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from subscriber.models import Subscriber
from django.conf import settings


def send_message(message):
    """Отправка уведомления в телеграмм"""
    bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
    try:
        bot.send_message(settings.CHAT_ID, message)
    except Exception as e:
        return HttpResponse('Произошла ошибка повторите позже.')


@api_view(['GET'])
def check(request, *args, **kwargs):
    """Отслеживание открытий писем"""
    id = request.query_params.get('id', None)
    id_sub = request.query_params.get('id_sub', None)
    if id is not None and id_sub is not None:
        name_sub = get_object_or_404(Subscriber, pk=id_sub)
        send_message(f'Письмо {id} у подписчика \
            {name_sub.first_name} {name_sub.last_name} открыто')
        return Response(status=201)
    return Response(status=404)
