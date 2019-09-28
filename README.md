# Educ
le projet comporte 5 applications

##blog_app

    ```

    from django.db import models
    from tinymce import HTMLField
    from django.contrib.auth.models import User

    # Create your models here.
    """Model definition for Blog"""

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



    ```

##education_app

    ```
    from django.db import models
    from tinymce import HTMLField
    from django.contrib.auth.models import User
    from django.db.models.signals import post_save
    from django.dispatch import receiver

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

    





    # Create your models here.


    #----------------------------------- USER -->> PROFILE --------------------------------#

    class Profile(models.Model):

        # Appel de user
    
        user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # 1 user <---> 1 profil
    
    
        # Champs suplementaires
        image = models.ImageField(upload_to='profile/', default='useravatar.png')
        is_prof = models.BooleanField(default=False)
        is_student = models.BooleanField(default=False)
        statut = models.BooleanField(default = True)
        date_add = models.DateTimeField(auto_now_add= True)
        date_update = models.DateTimeField(auto_now= True)

        # Initialisation a la creation
    
        @receiver(post_save, sender=User)
        def create_user_profile(sender, instance, created, **kwargs):
            if created:
                Profile.objects.create(user=instance)

        @receiver(post_save, sender=User)
        def save_user_profile(sender, instance, created, **kwargs):
        
            instance.profile.save()
        
    #python3 manage.py admin_generator eductaion_app >> eductaion_app/admin.py
    #./manage.py admin_generator APP_NAME >> APP_NAME/admin.py
    ```

##contact

    ```
    from django.db import models

    # Create your models here.
    class Contact_us(models.Model):
        """Model definition for Contact_us."""

        # TODO: Define fields here
        nom = models.CharField(max_length=50)
        email = models.EmailField()
        sujet = models.CharField(max_length=50)
        message = models.TextField()
        statut = models.BooleanField(default = True)
        date_add = models.DateTimeField(auto_now_add= True)
        date_update = models.DateTimeField(auto_now= True)

        class Meta:
            """Meta definition for Contact_us."""

            verbose_name = 'Contact_us'
            verbose_name_plural = 'Contact_uss'

        def __str__(self):
            """Unicode representation of Contact_us."""
            return "{} : {}".format(self.nom, self.sujet)


    class Newsletter(models.Model):
        """Model definition for Newsletter."""

        # TODO: Define fields here
        email = models.EmailField()
        statut = models.BooleanField(default = True)
        date_add = models.DateTimeField(auto_now_add= True)
        date_update = models.DateTimeField(auto_now= True)
    

        class Meta:
            """Meta definition for Newsletter."""

            verbose_name = 'Newsletter'
            verbose_name_plural = 'Newsletters'

        def __str__(self):
            """Unicode representation of Newsletter."""
            return self.email

    ```
    
##config