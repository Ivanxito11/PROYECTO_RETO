from django.db import models


class Docente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    edad= models.IntegerField(default=10)
    sexo=models.CharField(max_length=1) #1 es hombre y 2 es mujer
    email= models.EmailField(default = "ivanxito11@outlook.com")
    curso= models.IntegerField(default=1)
    user= models.CharField(max_length=100)
    user_mod= models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Docente"
        verbose_name_plural="Docentes"

    def __str__(self):
        return self.apellido + ' ' + self.nombre


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    user_mod = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="Pregunta"
        verbose_name="Pregunta"
        verbose_name_plural="Preguntas"
    def __str__(self):
        return self.pregunta

class Respuesta(models.Model):
    respuesta = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    user_mod = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table ="tr_Respuestas"
        verbose_name ="Respuesta"
        verbose_name_plural ="Respuestas"
    def __str__(self):
        return self.respuesta




