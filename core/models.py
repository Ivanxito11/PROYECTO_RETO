from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


from django.core import validators
from django.core.validators import RegexValidator, validate_email
from django.urls import reverse


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Rol(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)
    user = models.CharField(max_length=255)
    user_mod = models.CharField(max_length=15)
    fecha_ing = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "seg_rol"
        verbose_name = "rol"
        verbose_name_plural = "roles"

    def __str__(self):
        return '{}'.format(self.nombre)


class User(AbstractBaseUser):
    username = models.CharField(('username'), max_length=200, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[a-z0-9_-]*$',
            message='Usernames can only contain letters, numbers, underscores, and dashes.'
        )
    ])
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[validators.validate_email]
    )
    nombres= models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','date_of_birth']

    def __str__(self):
        return '{} {} {}'.format(self.username,self.nombres, self.apellidos)


    def get_absolute_url(self):
        return reverse('modificar_usuario', kwargs={'pk': self.pk})

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class RolUsuario(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)




class Curso(models.Model):
    docente= models.ForeignKey(User, on_delete=models.CASCADE)
    anio=models.CharField(max_length=20)
    paralelo=models.CharField(max_length=1)
    jornada=models.CharField(max_length=20)
    class Meta:
        db_table="Curso"
        verbose_name="Curso"
        verbose_name_plural="Cursos"
    def __str__(self):
        return '{} {} {}'.format(self.anio,self.paralelo,self.jornada)

class Tarea(models.Model):
    docente= models.ForeignKey(User, on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    descripcion=models.TextField(max_length=500)
    fecha= models.DateField(auto_now=True)
    puntaje= models.IntegerField(default=10)
    estado=models.BooleanField(default=True)
    class Meta:
        db_table="Tarea"
        verbose_name="Tareas"
        verbose_name_plural="Tareas"

class Actividad(models.Model):
    actividad = models.CharField(max_length=255)
    class Meta:
        db_table = "Actividad"
        verbose_name = "Actividad"
        verbose_name_plural = "Actividad"
    def __str__(self):
        return self.actividad


class Planificacion(models.Model):
    actividad= models.ForeignKey(Actividad, on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=500)
    fecha = models.DateField(auto_now_add=False)
    class Meta:
        db_table="Planificacion"
        verbose_name="Planificacion"
        verbose_name_plural="Planificaciones"

class Horario(models.Model):
    docente= models.ForeignKey(User, on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    hora= models.TimeField(auto_now=False, auto_now_add=False)
    dia= models.CharField(max_length=10)
    class Meta:
        db_table="Horario"
        verbose_name="Horario"
        verbose_name_plural="Horarios"


class Pregunta(models.Model):
    descripcion = models.CharField(max_length=200)
    puntaje = models.IntegerField(default=10)

    class Meta:
        db_table = "Pregunta"
        verbose_name = "pregunta"
        verbose_name_plural = "preguntas"

    def __str__(self):
        return self.descripcion


class Respuestas(models.Model):
    docente= models.ForeignKey(User, on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    estado_resp = models.BooleanField(default=1)

    class Meta:
        db_table = "Respuesta"
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"

    def __str__(self):
        return self.descripcion













