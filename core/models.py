from django.db import models

# Create your models here.
class Adresse(models.Model):
    nom = models.CharField(max_length=140)
    prenom = models.CharField(max_length=140)
    genre = models.CharField(max_length=140)
    email = models.EmailField()
    dob = models.DateField()
    pays = models.CharField(max_length=140)
    region = models.CharField(max_length=140)
    ville = models.CharField(max_length=140)
    profession = models.CharField(max_length=140)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.prenom, self.nom)
