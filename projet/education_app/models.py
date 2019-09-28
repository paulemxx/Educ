from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User

# Create your models here.
"""Model definition for Education"""

class Cours (models.Model):
    prof_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_cours')
    theme = models.ForeignKey('Theme', on_delete = models.CASCADE, related_name = 'them_cour')
    titre = models.CharField(max_length =225)
    numero = models.IntegerField()
    description = models.CharField(max_length=255)
    objectif = HTMLField('Objectif')
    prix = models.CharField(max_length=255)
    elgibilite = HTMLField('Eligibilite')
    nombre_place = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='img')
    programme_debut = models.TimeField(auto_now_add= False)
    programme_fin = models.TimeField(auto_now_add= False)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.nom

class chapitre (models.Model):
    cour_id = models.ForeignKey('Cours', on_delete = models.CASCADE, related_name = 'cour_chap')
    titre = models.CharField(max_length=255)
    contenue = HTMLField('contenue')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)
    
def __str__(self):
    return self.nom

class reviews (models.Model):
    prof_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_reviews')
    description = models.CharField(max_length =225)
    image = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Theme (models.Model):
    titre = models.CharField(max_length =225)
    image = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

    


