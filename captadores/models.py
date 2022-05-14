from django.db import models
class Captador(models.Model):

    marca = models.CharField(max_length=30)
    bobina = models.CharField(max_length=9)
    instrumento = models.CharField(max_length=10)

    def __str__(self):
        return self.marca 

