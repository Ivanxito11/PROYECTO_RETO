"""appdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    #USUARIOS
    path('consultar_usuarios/', views.consultarusuarios, name="consultar_usuarios"),
    path('crear_usuario/', views.crearusuario, name="crear_usuario"),
    path('modificar_usuario/<int:pk>', views.modificarusuario, name="modificar_usuario"),
    path('eliminar_usuario/<int:pk>', views.eliminarusuario, name="eliminar_usuario"),

    #ROLES
    path('crear_rol/', views.crear_rol, name="crear_rol"),
    path('mostrar_roles/', views.mostrar_roles, name="mostrar_roles"),
    path('modificar_roles/<int:pk>', views.modificar_roles, name="modificar_roles"),
    path('eliminar_roles/<int:pk>', views.eliminar_roles, name="eliminar_roles"),

    #ROLESXUSUARIO
    path('crear_rol_usuario/', views.crear_rol_usuario, name="crear_rol_usuario"),
    path('mostrar_roles_usuarios/', views.mostrar_roles_usuarios, name="mostrar_roles_usuarios"),
    path('modificar_roles_usuarios/<int:pk>', views.modificar_roles_usuarios, name="modificar_roles_usuarios"),
    path('eliminar_rol_usuario/<int:pk>', views.eliminar_rol_usuario, name="eliminar_rol_usuario"),

    #CURSOS
    path('crearcurso/', views.crearcurso, name="crearcurso"),
    path('mostrarcursos/', views.mostrarcursos, name="mostrarcursos"),
    path('modificarcurso/<int:pk>', views.modificarcurso, name="editarcursos"),
    path('eliminarcurso/<int:pk>', views.eliminarcurso, name="eliminarcurso"),


    #TAREAS
    path('creartarea/', views.creartarea, name="creartarea"),
    path('mostrartareas/', views.mostrartareas, name="mostrartareas"),
    path('modificartarea/<int:pk>', views.modificartarea, name="modificartarea"),
    path('eliminartarea/<int:pk>', views.eliminartarea, name="eliminartarea"),

    #PLANIFICACIONES
    path('crearplanificacion/', views.crearplanificacion, name="crearplanificacion"),
    path('mostrarplanificaciones/', views.mostrarplanificacion, name="mostrarplanificaciones"),
    path('modificarplanificacion/<int:pk>', views.modificarplanificacion, name="modificarplanificacion"),
    path('eliminarplanificacion/<int:pk>', views.eliminarplanificacion, name="eliminarplanificacion"),

    #HORARIOS
    path('crearhorario/', views.crearhorario, name="crearhorario"),
    path('mostrarhorario/', views.mostrarhorario, name="mostrarhorario"),
    path('modificarhorario/<int:pk>', views.modificarhorario, name="modificarhorario"),
    path('eliminarhorario/<int:pk>', views.eliminarhorario, name="eliminarhorario"),

    #PREGUNTA
    path('crearpregunta/', views.crearpregunta, name="crearpregunta"),
    path('mostrarpregunta/', views.mostrarpregunta, name="mostrarpregunta"),
    path('modificarpregunta/<int:pk>', views.modificarpregunta, name="modificarpregunta"),
    path('eliminarpregunta/<int:pk>', views.eliminarpregunta, name="eliminarpregunta"),

    #RESPUESTAS
    path('crear_respuesta/', views.crear_respuesta, name="crear_respuesta"),
    path('mostrar_respuestas/', views.mostrar_respuesta, name="mostrar_respuestas"),
    path('modificar_respuesta/<int:pk>', views.modificar_respuesta, name="modificar_respuesta"),
    path('eliminar_respuesta/<int:pk>', views.eliminar_respuesta, name="eliminar_respuesta"),

    #ACTIVIDAD
    path('crearactividad/', views.crearactividad, name="crearactividad"),
    path('mostraractividades/', views.mostraractividad, name="mostraractividades"),
    path('modificaractividad/<int:pk>', views.modificaractividad, name="modificaractividad"),
    path('eliminaractividad/<int:pk>', views.eliminaractividad, name="eliminaractividad"),


    path('tareas/', views.tareas, name="tareas"),
    path('horarios/', views.horarios, name="horarios"),
    path('examenes/', views.examenes, name="examenes"),
    path('planificaciones/', views.planificaciones, name="planificaciones"),



    path('admin/', admin.site.urls)
]
