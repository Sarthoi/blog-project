from django.db import models

# Create your models here.


class Games(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    precio=models.IntegerField()
    stock=models.IntegerField()
    plataforma=models.IntegerField()
    imagen = models.ImageField(upload_to='games/', null=True) 