from django.db import models

class Project(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    user= models.CharField(max_length=100)
    user_mod= models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
class Estudiantes(models.Model):
    nombre=models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    edad= models.IntegerField
    sexo=models.CharField(max_length=1)
    email= models.EmailField
    user= models.CharField(max_length=100)
    user_mod= models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="estudiante"
        verbose_name_plural="estudiantes"


# Create your models here.
