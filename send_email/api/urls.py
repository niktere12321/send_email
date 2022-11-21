from django.conf.urls import url

from . import views

app_name = 'api'


urlpatterns = [
    url('^check/', views.check),
]
