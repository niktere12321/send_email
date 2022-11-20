from rest_framework.response import Response
from django.http import HttpResponse
import telegram
from django.conf import settings
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import renderers
from rest_framework.decorators import api_view
from subscriber.models import Subscriber
import os


TELEGRAM_TOKEN = '2033287598:AAFBPr75b4abzYk0rMSH2Q4ph9mvMmC1U38'
CHAT_ID = '1495697329'

bot = telegram.Bot(token=TELEGRAM_TOKEN)


def send_message(message):
    """Отправка сообщение администратору в телеграмм"""
    text = message
    try:
        bot.send_message(CHAT_ID, text)
    except Exception as e:
        return HttpResponse('Произошла ошибка повторите позже.')


@api_view(['GET'])
def check(request, *args, **kwargs):
    id = request.query_params.get('id', None)
    if id is not None:
        print(1)
        # name_sub = get_object_or_404(Subscriber, id_sub) {name_sub.first_name} {name_sub.last_name}
        send_message(f'Письмо {id} у подписчика  открыто')
        # pixel = JPEGRenderer().render(self=None, data=open(os.path.join(settings.STATIC_DIR, 'img\pixel.jpg'), 'rb'))
        return Response(status=201)
    return Response(status=404)


class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


# class Check(APIView):
#     renderer_classes = [JPEGRenderer]

#     @property
#     def pixel(self):
#         return open(os.path.join(settings.STATIC_DIR, 'img\pixel.jpg'), 'rb')

#     def get(self, request, *args, **kwargs):
#         id = request.query_params.get('id', None)
#         # id_sub = request.query_params.get('id_sub', None)
#         if id is not None:
#             print(1)
#             # name_sub = get_object_or_404(Subscriber, id_sub) {name_sub.first_name} {name_sub.last_name}
#             send_message(f'Письмо {id} у подписчика  открыто')
#             return Response(self.pixel.read(), status=201)
#         return Response(status=404)
