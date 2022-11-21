from django.urls import path

from . import views

app_name = 'send'


urlpatterns = [
    path('', views.index, name='index'),
    path('create_mailing/', views.create_mailing, name='create_mailing'),
    path('get_mailing/<int:id>', views.get_mailing, name='get_mailing'),
]
