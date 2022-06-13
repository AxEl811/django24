from django.db import models

# Create your models here.
class Machines(models.Model):
    id= models.AutoField(
            primary_key=True,
            editable=False)

    utilisateur= models.CharField(
        blank=True,
        null=True,
        max_length=200)
     
    adresse= models.CharField(
        blank=True,
        null=True,
        max_length=200)
    adresse= models.CharField(
        blank=True,
        null=True,
        max_length=200)

    masque= models.CharField(
        blank=True,
        null=True,
        max_length=200)
    
    nom_du_reseau= models.CharField(
        blank=True,
        null=True,
        max_length=200)
        
    mises_a_jour= models.CharField(
        blank=True,
        null=True,
        max_length=200)
    
    technicien_qui_a_fait_la_mise_a_jour= models.CharField(
        blank=True,
        null=True,
        max_length=200)
    
    date_de_la_mises_a_jour= models.DateField()
