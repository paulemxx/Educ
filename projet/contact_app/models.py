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
