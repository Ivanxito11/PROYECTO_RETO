import io
from django.http import FileResponse
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

from .forms import UserCreationForm, RolForm, RolUsuarioForm,CursoForm, Tareaform, Planificacionform, Horarioform, Ingresopreguntaform, IngresoRespuestaform,Actividadform
from .models import User, Rol, RolUsuario,Curso,Tarea,Planificacion, Horario, Pregunta, Respuestas,Actividad



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
    usuarios_roles = RolUsuario.objects.all()
    return render(request,"mostrar_roles_usuarios.html",{'usuario_roles':usuarios_roles})

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

#---------------------------------------------------------------------------------------------------------
# CRUDS DE TAREAS

def creartarea(request, plantilla="creartarea.html"):
    if request.method == "POST":
        tareaform = Tareaform(request.POST or None)
        if tareaform.is_valid():
            tarea = tareaform.save(commit=False)
            tarea.docente = request.user
            tarea.save()
        return redirect("mostrartareas")
    else:
        tarea = Tareaform()
    return render(request, plantilla, {'tarea': tarea})

def mostrartareas(request):
    tarea= Tarea.objects.filter(docente_id= request.user.id)
    return render(request, "mostrartarea.html", {'tarea': tarea})

def modificartarea(request, pk, plantilla="modificartarea.html"):
    if request.method == "POST":
        tarea = get_object_or_404(Tarea, id=pk)
        tareaform = Tareaform(request.POST or None, instance=tarea)
        if tareaform.is_valid():
            tareaform.save()
        return redirect("mostrartareas")
    else:
        tarea = get_object_or_404(Tarea, id=pk)
        tareaform = Tareaform(request.POST or None, instance=tarea)
    return render(request, plantilla, {'tareaform': tareaform})


def eliminartarea(request, pk, plantilla="eliminartarea.html"):
    if request.method == "POST":
        tarea = get_object_or_404(Tarea, pk=pk)
        tareaform = Tareaform(request.POST or None, instance=tarea)
        if tareaform.is_valid():
            tarea.delete()
        return redirect('mostrartareas')
    else:
        tarea = get_object_or_404(Tarea, pk=pk)
        tareaform = Tareaform(request.POST or None, instance=tarea)
    return render(request, plantilla, {'tareaform': tareaform})

#-----------------------------------------------------------------------------------------------
#CRUD DE PLANIFICACIONES

def crearplanificacion(request, plantilla="crearplanificacion.html"):
    if request.method == "POST":
        planificacionform = Planificacionform(request.POST or None)
        if planificacionform.is_valid():
            planificacion = planificacionform.save(commit=False)
            planificacion.docente = request.user
            planificacion.save()
        return redirect("mostrarplanificaciones")
    else:
        planificacion = Planificacionform()
    return render(request, plantilla, {'planificacion': planificacion})


def mostrarplanificacion(request):
    planificacion= Planificacion.objects.filter(docente_id= request.user.id)
    return render(request, "mostrarplanificacion.html", {'planificacion': planificacion})


def modificarplanificacion(request, pk, plantilla="modificarplanificacion.html"):
    if request.method == "POST":
        planificacion = get_object_or_404(Planificacion, id=pk)
        planificacionform = Planificacionform(request.POST or None, instance=planificacion)
        if planificacionform.is_valid():
            planificacionform.save()
        return redirect("mostrarplanificaciones")
    else:
        planificacion = get_object_or_404(Planificacion, id=pk)
        planificacionform = Planificacionform(request.POST or None, instance=planificacion)
    return render(request, plantilla, {'planificacionform': planificacionform})


def eliminarplanificacion(request, pk, plantilla="eliminarplanificacion.html"):
    if request.method == "POST":
        planificacion = get_object_or_404(Planificacion, pk=pk)
        planificacionform = Planificacionform(request.POST or None, instance=planificacion)
        if planificacionform.is_valid():
            planificacion.delete()
        return redirect('mostrarplanificaciones')
    else:
        planificacion = get_object_or_404(Planificacion, pk=pk)
        planificacionform = Planificacionform(request.POST or None, instance=planificacion)
    return render(request, plantilla, {'planificacionform': planificacionform})

#-----------------------------------------------------------------------------------------------------
#CRUD HORARIO

def crearhorario(request, plantilla="crearhorario.html"):
    if request.method == "POST":
        horario = Horarioform(request.POST or None)
        if horario.is_valid():
            horario.save()
        return redirect("mostrarhorario")
    else:
        horario = Horarioform()
    return render(request, plantilla, {'horario': horario})


def mostrarhorario(request):
    horario = Horario.objects.all()
    return render(request, "mostrarhorario.html", {'horario': horario})


def modificarhorario(request, pk, plantilla="modificarhorario.html"):
    if request.method == "POST":
        horario = get_object_or_404(Horario, id=pk)
        horarioform = Horarioform(request.POST or None, instance=horario)
        if horarioform.is_valid():
            horarioform.save()
        return redirect("mostrarhorario")
    else:
        horario = get_object_or_404(Horario, id=pk)
        horarioform = Horarioform(request.POST or None, instance=horario)
    return render(request, plantilla, {'horarioform': horarioform})


def eliminarhorario(request, pk, plantilla="eliminarhorario.html"):
    if request.method == "POST":
        horario = get_object_or_404(Horario, pk=pk)
        horarioform = Horarioform(request.POST or None, instance=horario)
        if horarioform.is_valid():
            horario.delete()
        return redirect('mostrarhorario')
    else:
        horario = get_object_or_404(Horario, pk=pk)
        horarioform = Horarioform(request.POST or None, instance=horario)
    return render(request, plantilla, {'horarioform': horarioform})


#----------------------------------------------------------------------------------------------------------
#CRUD PREGUNTA

def crearpregunta(request, plantilla="crearpregunta.html"):
    if request.method == "POST":
        preguntaform = Ingresopreguntaform(request.POST or None)
        if preguntaform.is_valid():
            pregunta = preguntaform.save(commit=False)
            pregunta.docente = request.user
            pregunta.save()
        return redirect("mostrarpregunta")
    else:
        pregunta = Ingresopreguntaform()
    return render(request, plantilla, {'pregunta': pregunta})

def mostrarpregunta(request):
    pregunta= Pregunta.objects.filter(docente_id= request.user.id)
    return render(request, "mostrarpreguntas.html", {'pregunta': pregunta})


def modificarpregunta(request, pk, plantilla="modificarpregunta.html"):
    if request.method == "POST":
        pregunta = get_object_or_404(Pregunta, id=pk)
        preguntaform = Ingresopreguntaform(request.POST or None, instance=pregunta)
        if preguntaform.is_valid():
            preguntaform.save()
        return redirect("mostrarpregunta")
    else:
        pregunta = get_object_or_404(Pregunta, id=pk)
        preguntaform = Ingresopreguntaform(request.POST or None, instance=pregunta)
    return render(request, plantilla, {'preguntaform': preguntaform})


def eliminarpregunta(request, pk, plantilla="eliminarpregunta.html"):
    if request.method == "POST":
        pregunta = get_object_or_404(Pregunta, pk=pk)
        preguntaform = Ingresopreguntaform(request.POST or None, instance=pregunta)
        if preguntaform.is_valid():
            pregunta.delete()
        return redirect('mostrarpregunta')
    else:
        pregunta = get_object_or_404(Pregunta, pk=pk)
        preguntaform = Ingresopreguntaform(request.POST or None, instance=pregunta)
    return render(request, plantilla, {'preguntaform': preguntaform})


#-----------------------------------------------------------------------------------------------------------
#CRUD RESPUESTA

def crear_respuesta(request, plantilla="crear_respuesta.html"):
    if request.method == "POST":
        respuestaform = IngresoRespuestaform(request.POST or None)
        if respuestaform.is_valid():
            respuesta = respuestaform.save(commit=False)
            respuesta.docente = request.user
            respuesta.save()
        return redirect("mostrar_respuestas")
    else:
        respuesta = IngresoRespuestaform()
    return render(request, plantilla, {'respuesta': respuesta})

def mostrar_respuesta(request):
    respuesta= Respuestas.objects.filter(docente_id= request.user.id)
    return render(request, "mostrar_respuestas.html", {'respuesta': respuesta})


def modificar_respuesta(request, pk, plantilla="modificar_respuesta.html"):
    if request.method == "POST":
        respuesta = get_object_or_404(Respuestas, id=pk)
        respuestaform = IngresoRespuestaform(request.POST or None, instance=respuesta)
        if respuestaform.is_valid():
            respuestaform.save()
        return redirect("mostrar_respuestas")
    else:
        respuesta = get_object_or_404(Respuestas, id=pk)
        respuestaform= IngresoRespuestaform(request.POST or None, instance=respuesta)
    return render(request, plantilla, {'respuestaform': respuestaform})


def eliminar_respuesta(request, pk, plantilla="eliminar_respuesta.html"):
    if request.method == "POST":
        respuesta = get_object_or_404(Respuestas, pk=pk)
        respuestaform = Ingresopreguntaform(request.POST or None, instance=respuesta)
        if respuestaform.is_valid():
            respuesta.delete()
        return redirect('mostrar_respuestas')
    else:
        respuesta = get_object_or_404(Respuestas, pk=pk)
        respuestaform = IngresoRespuestaform(request.POST or None, instance=respuesta)
    return render(request, plantilla, {'respuestaform': respuestaform })

#--------------------------------------------------------------------------------------------
#CRUD DE ACTIVIDAD
def crearactividad(request, plantilla="crearactividad.html"):
    if request.method == "POST":
        actividad =Actividadform(request.POST or None)
        if actividad.is_valid():
            actividad.save()
        return redirect("mostraractividades")
    else:
        actividad = Actividadform()
    return render(request, plantilla, {'actividad': actividad})


def mostraractividad(request):
    actividad = Actividad.objects.all()
    return render(request, "mostraractividades.html", {'actividad': actividad})


def modificaractividad(request, pk, plantilla="modificaractividad.html"):
    if request.method == "POST":
        actividad = get_object_or_404(Actividad, id=pk)
        actividadform = Actividadform(request.POST or None, instance=actividad)
        if actividadform.is_valid():
            actividadform.save()
        return redirect("mostraractividades")
    else:
        actividad = get_object_or_404(Actividad, id=pk)
        actividadform= Actividadform(request.POST or None, instance=actividad)
    return render(request, plantilla, {'actividadform': actividadform})


def eliminaractividad(request, pk, plantilla="eliminaractividad.html"):
    if request.method == "POST":
        actividad = get_object_or_404(Actividad, pk=pk)
        actividadform = Actividadform(request.POST or None, instance=actividad)
        if actividadform.is_valid():
            actividad.delete()
        return redirect('mostraractividades')
    else:
        actividad = get_object_or_404(Actividad, pk=pk)
        actividadform = Actividadform(request.POST or None, instance=actividad)
    return render(request, plantilla, {'actividadform': actividadform })


#---------------------------------------------------------------------------------------
#REPORTERIA DE LISTADOS

def exportarListTareas(request, plantilla="mostrartarea.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_tareas.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    tareas = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Tareas", styles['Heading1'])
    tareas.append(header)
    headings = ('Id', 'Curso', 'Descripcion', 'Fecha', 'Puntaje', 'Asignado')
    tareas = [(d.id, d.curso, d.descripcion , d.fecha,d.puntaje,d.estado) for d in Tarea.objects.all()]
    print(tareas)

    t = Table([headings] + tareas)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    tareas.append(t)
    doc.build(tareas)
    response.write(buffer.getvalue())
    buffer.close()
    return response

# Create your views here.
