from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

from .forms import UserCreationForm, RolForm, RolUsuarioForm,CursoForm
from .models import User, Rol, RolUsuario,Curso



html_base = """
    <h1>MENU DE GESTION DE DOCENTES</h1>
    <ul>
        <li>   <a href="/">Portada</a>              </li>
        <li>   <a href="/tareas/">tareas</a>   </li>
        <li>   <a href="/horarios/">horarios</a>     </li>
        <li>   <a href="/examenes/">examenes</a>     </li>
        <li>   <a href="/planificaciones/">planificaciones</a>     </li>
        <li>   <a href="/cronograma/">cronograma</a>     </li>
    </ul>
"""



def home(request, plantilla="home.html"):
    return render(request, plantilla);

def horarios(request, plantilla="horarios.html"):
    return render(request, plantilla);


def tareas(request, plantilla="tareas.html"):
    return render(request, plantilla);


def examenes(request, plantilla="examenes.html"):
    return render(request, plantilla);


def planificaciones(request, plantilla="planificaciones.html"):
    return render(request, plantilla);

def cronograma(request, plantilla="cronograma.html"):
    return render(request, plantilla);

def modelo1(request, plantilla="modelo1.html"):
    return render(request, plantilla);

def registro(request, plantilla="registro.html"):
    return render(request, plantilla);


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect("home")

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect("login")

#CRUD DE USUARIOS

def crearusuario(request, plantilla="crearusuario.html"):
    if request.method=="POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('consultar_usuarios')
    else:
        form=UserCreationForm()
    return render(request, plantilla, {'form':form})

def consultarusuarios(request, plantilla="consultarusuario.html"):
    usuarios = User.objects.all
    return render(request, plantilla, {'usuarios':usuarios})

def modificarusuario(request, pk, plantilla="modificarusuario.html"):
    if request.method=="POST":
        usuario = get_object_or_404(User, pk=pk)
        form = UserCreationForm(request.POST or None, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('consultar_usuarios')
    else:
        usuario = get_object_or_404(User, pk=pk)
        form = UserCreationForm(request.POST or None, instance=usuario)
    return render(request, plantilla, {'form':form})


def eliminarusuario(request, pk, plantilla="eliminarusuario.html"):
    if request.method=="POST":
        usuario = get_object_or_404(User, pk=pk)
        form = UserCreationForm(request.POST or None, instance=usuario)
        if form.is_valid():
            usuario.delete()
        return redirect('consultar_usuarios')
    else:
        usuario = get_object_or_404(User, pk=pk)
        form = UserCreationForm(request.POST or None, instance=usuario)
    return render(request, plantilla, {'form':form})

#-----------------------------------------------------------------------------------------------------#

#CRUDS DE ROLES
def crear_rol(request, plantilla="crear_rol.html"):
    if request.method == "POST":
        rol = RolForm(request.POST or None)
        if rol.is_valid():
            rol.save()
        return redirect("mostrar_roles")
    else:
        rol = RolForm()
    return render(request, plantilla, {'rol': rol})


def mostrar_roles(request):
    roles = Rol.objects.all()
    return render(request,"mostrar_roles.html",{'roles':roles})


def modificar_roles(request,pk,plantilla="modificar_roles.html"):
    if request.method == "POST":
        rol=get_object_or_404(Rol, id=pk)
        rolform= RolForm(request.POST or None, instance=rol)
        if rolform.is_valid():
            rolform.save()
        return redirect("mostrar_roles")
    else:
        rol=get_object_or_404(Rol,id=pk)
        rolform = RolForm(request.POST or None, instance=rol)
    return render(request,plantilla,{'rolform': rolform})

def eliminar_roles(request, pk, plantilla="eliminar_roles.html"):
    if request.method=="POST":
        rol = get_object_or_404(Rol, pk=pk)
        form = RolForm(request.POST or None, instance=rol)
        if form.is_valid():
            rol.delete()
        return redirect('mostrar_roles')
    else:
        rol = get_object_or_404(Rol, pk=pk)
        form = RolForm(request.POST or None, instance=rol)
    return render(request, plantilla, {'form':form})

#------------------------------------------------------------------------------------------------------#
#CRUDS ROLESUSUARIOS
def crear_rol_usuario(request, plantilla="crear_rol_usuario.html"):
    if request.method=="POST":
        form = RolUsuarioForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('mostrar_roles_usuarios')
    else:
        form=RolUsuarioForm()
    return render(request, plantilla, {'form':form})

def mostrar_roles_usuarios(request):
    usuario_roles = RolUsuario.objects.all()
    return render(request,"mostrar_roles_usuarios.html",{'usuario_roles':usuario_roles})

def modificar_roles_usuarios(request,pk,plantilla="modificar_roles_usuarios.html"):
    if request.method == "POST":
        rolusuario=get_object_or_404(RolUsuario, id=pk)
        rolform= RolUsuarioForm(request.POST or None, instance=rolusuario)
        if rolform.is_valid():
            rolform.save()
        return redirect("mostrar_roles_usuarios")
    else:
        rolusuario=get_object_or_404(RolUsuario,id=pk)
        rolform = RolUsuarioForm(request.POST or None, instance=rolusuario)
    return render(request,plantilla,{'rolform': rolform})

def eliminar_rol_usuario(request, pk, plantilla="eliminar_rol_usuario.html"):
    if request.method=="POST":
        rol = get_object_or_404(RolUsuario, pk=pk)
        form = RolUsuarioForm(request.POST or None, instance=rol)
        if form.is_valid():
            rol.delete()
        return redirect('mostrar_roles_usuarios')
    else:
        rol = get_object_or_404(RolUsuario, pk=pk)
        form = RolUsuarioForm(request.POST or None, instance=rol)
    return render(request, plantilla, {'form':form})

#---------------------------------------------------------------------------------------------------------#
#CRUD DE CURSOS
def crearcurso(request, plantilla="crearcurso.html"):
    if request.method == "POST":
        curso = CursoForm(request.POST or None)
        if curso.is_valid():
            curso.save()
        return redirect("mostrarcursos")
    else:
        curso = CursoForm()
    return render(request, plantilla, {'curso': curso})


def mostrarcursos(request):
    curso = Curso.objects.all()
    return render(request,"mostrarcursos.html",{'curso':curso})

def modificarcurso(request,pk,plantilla="editarcursos.html"):
    if request.method == "POST":
        curso=get_object_or_404(Curso, id=pk)
        cursoform= CursoForm(request.POST or None, instance=curso)
        if cursoform.is_valid():
            cursoform.save()
        return redirect("mostrarcursos")
    else:
        curso=get_object_or_404(Curso,id=pk)
        cursoform = CursoForm(request.POST or None, instance=curso)
    return render(request,plantilla,{'cursoform': cursoform})

def eliminarcurso(request, pk, plantilla="eliminarcurso.html"):
    if request.method=="POST":
        curso = get_object_or_404(Curso, pk=pk)
        form = CursoForm(request.POST or None, instance=curso)
        if form.is_valid():
            curso.delete()
        return redirect('mostrarcursos')
    else:
        curso = get_object_or_404(Curso, pk=pk)
        form = CursoForm(request.POST or None, instance=curso)
    return render(request, plantilla, {'form':form})


# Create your views here.
