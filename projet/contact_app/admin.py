from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class Contact_usAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'email',
        'sujet',
        'message',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'nom',
        'email',
        'sujet',
        'message',
        'statut',
        'date_add',
        'date_update',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'statut', 'date_add', 'date_update')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'email',
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact_us, Contact_usAdmin)
_register(models.Newsletter, NewsletterAdmin)
