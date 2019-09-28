from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User

# Create your models here.

class Categorie (models.Model):
    nom = models.CharField(max_length=225)
    titre = models.CharField(max_length =225)
    image = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.nom

class Artcle (models.Model):
    categorie = models.ForeignKey('Categorie', on_delete = models.CASCADE, related_name = 'categorie_article')
    auteur = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_article')
    tag = models.ManyToManyField("Tag")
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=225)
    contenue = HTMLField('contenue')
    image = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)
    
def __str__(self):
    return self.nom

class Commentaire (models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_commentaire')
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=225)
    image = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Tag (models.Model):
    titre = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)


