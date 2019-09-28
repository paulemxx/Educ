from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'titre',
        'image',
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
        'titre',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


class ArtcleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'auteur',
        'titre',
        'description',
        'contenue',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'categorie',
        'auteur',
        'statut',
        'date_add',
        'date_update',
        'id',
        'categorie',
        'auteur',
        'titre',
        'description',
        'contenue',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    raw_id_fields = ('tag',)


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user_id',
        'titre',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'user_id',
        'statut',
        'date_add',
        'date_update',
        'id',
        'user_id',
        'titre',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'statut', 'date_add', 'date_update')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'titre',
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Artcle, ArtcleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Tag, TagAdmin)
