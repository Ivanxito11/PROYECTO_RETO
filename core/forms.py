from django import forms
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError



class RolForm(forms.ModelForm):
    class Meta:
        model= Rol
        fields=['nombre']

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','nombres','apellidos', 'email', 'date_of_birth')
        widgets = {'date_of_birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date'})}


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class RolUsuarioForm(forms.ModelForm):
    class Meta:
        model = RolUsuario
        fields = ['rol', 'usuario']

class CursoForm(forms.ModelForm):
    class Meta:
        model= Curso
        fields=['docente','anio','paralelo','jornada']

class Tareaform(forms.ModelForm):
    class Meta:
        model= Tarea
        fields= ['curso','descripcion','puntaje','estado']

class Actividadform(forms.ModelForm):
    class Meta:
        model= Actividad
        fields=['actividad']

class Planificacionform(forms.ModelForm):
    class Meta:
        model= Planificacion
        fields= ['actividad','curso','descripcion','fecha']
        widgets = {'fecha': forms.DateInput(format=('%m/%d/%Y'),attrs={'type':'date' })}



class Horarioform(forms.ModelForm):
    class Meta:
        model= Horario
        fields= ['docente','curso','hora','dia']
        widgets = {'hora': forms.TimeInput(format=('%h:%m:%s'), attrs={'type': 'time'})}


class Ingresopreguntaform(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields=['descripcion','puntaje']

class IngresoRespuestaform(forms.ModelForm):
    class Meta:
        model= Respuestas
        fields=['curso','id_pregunta','descripcion','estado_resp']

