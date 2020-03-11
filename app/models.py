from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=True)
    sobrenome = models.CharField(max_length=30, null=True, blank=True)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome