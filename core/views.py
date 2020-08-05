from django.http import HttpResponse
from django.shortcuts import render

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

def home(request):
    html_responsde = "<h1>la pagina de portada</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def login(request):
    html_responsde = "<h1>la pagina de portada</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def horarios(request):
    html_responsde = "<h1>la pagina de contacto</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def tareas(request):
    html_responsde = "<h1>la pagina de acerca de</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def examenes(request):
    html_responsde = "<h1>la pagina de quienes somos</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def planificaciones(request):
    html_responsde = "<h1>la pagina de servicios</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)
def cronograma(request):
    html_responsde = "<h1>la pagina de cronogramas</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)
def modelo1(request):
    html_responsde = "<h1>la pagina de modelo 1</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def registro(request):
    html_responsde = "<h1>la pagina de registro</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def home(request, plantilla="home.html"):
    return render(request, plantilla);

def login(request, plantilla="login.html"):
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

# Create your views here.
