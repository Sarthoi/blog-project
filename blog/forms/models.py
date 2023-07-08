from django.db import models

# Create your models here.

class Users(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=150)
    staff=models.IntegerField

class Games(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    precio=models.IntegerField()
    stock=models.IntegerField()
    plataforma=models.IntegerField()