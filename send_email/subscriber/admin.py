from django.contrib import admin

from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'email',
        'birthday',
        'first_name',
        'last_name',
    )
    search_fields = ('email', 'birthday', 'last_name')
    empty_value_display = '-пусто-'


admin.site.register(Subscriber, SubscriberAdmin)
