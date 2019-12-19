from django.db import models

from enum import Enum

# Create your models here.
class Adresse(models.Model):
    class SEX(Enum):
        Male = ('Male', 'male')
        Female = ('Female', 'female')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    class REGION(Enum):
        Adamaoua = ('Adamaoua', 'adamaoua')
        Centre = ('Centre', 'centre')
        Est = ('Est', 'est')
        Extreme_Nord = ('Extreme-Nord', 'extreme nord')
        Littoral = ('Littoral', 'littoral')
        Nord = ('Nord', 'nord')
        Nord_Ouest = ('Nord-Ouest', 'nord ouest')
        Ouest = ('Ouest', 'ouest')
        Sud = ('Sud', 'sud')
        Sud_Ouest = ('Sud-Ouest', 'sud ouest')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    class PAYS(Enum):
        CMR = ('CMR', 'Cameroun')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    class PROFESSION(Enum):
        AGR = ('AGR', 'Agriculteur')
        ETU = ('ETU', 'Etudiant')
        MEN = ('MEN', 'Menagere')
        OUV = ('OUV', 'Ouvrier')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    nom = models.CharField(max_length=140)
    prenom = models.CharField(max_length=140)
    genre = models.CharField(max_length=140, choices=[x.value for x in SEX], default=SEX.get_value('Female'),)
    email = models.EmailField()
    dob = models.DateField()
    pays = models.CharField(max_length=140, choices=[x.value for x in PAYS], default=PAYS.get_value('CMR'),)
    region = models.CharField(max_length=140, choices=[x.value for x in REGION], default=REGION.get_value('Adamaoua'), )
    ville = models.CharField(max_length=140)
    profession = models.CharField(max_length=140, choices=[x.value for x in PROFESSION], default=PROFESSION.get_value('MEN'),)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.prenom, self.nom)
