from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CoursAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'prof_id',
        'theme',
        'titre',
        'numero',
        'description',
        'objectif',
        'prix',
        'elgibilite',
        'nombre_place',
        'image',
        'programme_debut',
        'programme_fin',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'prof_id',
        'theme',
        'statut',
        'date_add',
        'date_update',
        'id',
        'prof_id',
        'theme',
        'titre',
        'numero',
        'description',
        'objectif',
        'prix',
        'elgibilite',
        'nombre_place',
        'image',
        'programme_debut',
        'programme_fin',
        'statut',
        'date_add',
        'date_update',
    )


class chapitreAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'cour_id',
        'titre',
        'contenue',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'cour_id',
        'statut',
        'date_add',
        'date_update',
        'id',
        'cour_id',
        'titre',
        'contenue',
        'statut',
        'date_add',
        'date_update',
    )


class reviewsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'prof_id',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'prof_id',
        'statut',
        'date_add',
        'date_update',
        'id',
        'prof_id',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


class ThemeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
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
        'titre',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'image',
        'is_prof',
        'is_student',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'user',
        'is_prof',
        'is_student',
        'statut',
        'date_add',
        'date_update',
        'id',
        'user',
        'image',
        'is_prof',
        'is_student',
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Cours, CoursAdmin)
_register(models.chapitre, chapitreAdmin)
_register(models.reviews, reviewsAdmin)
_register(models.Theme, ThemeAdmin)
_register(models.Profile, ProfileAdmin)
