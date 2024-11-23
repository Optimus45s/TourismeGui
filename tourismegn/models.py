from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Site(models.Model):
    TYPES = [
        ('nature', 'Nature'),
        ('culture', 'Culture'),
    ]
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPES)
    description = models.TextField()
    historique = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='images/sites/', default='images/default-site.jpg')             
    def __str__(self):
        return self.nom

class Hotel(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    description = models.TextField()
    prix_nuit = models.DecimalField(max_digits=6, decimal_places=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    site_rel = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="hotels")
    image = models.ImageField(upload_to='images/sites/', default='images/default-hotel.jpg')

    def __str__(self):
        return self.nom

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    client = models.CharField(max_length=100)
    site = models.ForeignKey('Site', on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, null=True, blank=True)
    date_reservation = models.DateTimeField(null=True, blank=True)  # Retirer auto_now_add
    date_visite = models.DateField(null=True, blank=True)
    nombre_personnes = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[('confirmée', 'Confirmée'), ('en attente', 'En attente')], default='en attente')

    def __str__(self):
        if self.site:
            return f"Réservation pour {self.site.nom} par {self.user.username}"
        elif self.hotel:
            return f"Réservation pour {self.hotel.nom} par {self.user.username}"



    
class BlogPost(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_posts/', blank=True, null=True)

    def __str__(self):
        return self.titre

