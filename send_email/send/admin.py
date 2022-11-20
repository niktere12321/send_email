from django.contrib import admin

from .models import MailingEmail


class MailingEmailAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'text',
        'pub_date',
    )


admin.site.register(MailingEmail, MailingEmailAdmin)
