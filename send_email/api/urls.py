from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'api'


urlpatterns = [
    # path('check/<int:id_message>/<int:id_sub>', views.Check.as_view(), name='check'),
    # url('^check/', views.Check.as_view(), name='check'),
    url('^check/', views.check),
]
