from django.db import models

# Create your models here.

class Enseignant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField()
    diplome = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Enseignants"

    def __str__(self):
        return self.nom
