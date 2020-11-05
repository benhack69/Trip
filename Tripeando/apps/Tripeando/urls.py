from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from .views import Inicio,Lugares,Blog,Crearpost,Perfil,Postvista,Registro,iniciar_sesion,registrar,guardarpost

urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('lugares/',Lugares,name="Lugares"),
    path('blog/',Blog,name="Blog"),
    path('crearpost/',Crearpost,name="Crearpost"),
    path('login/',LoginView.as_view(template_name='Tripeando/login.html'),name="iniciar_sesion"),
    path('logout/',LogoutView.as_view(template_name='Tripeando/index.html'),name="logout"),
    path('perfil/',Perfil,name="Perfil"),
    path('post/',Postvista,name="Post"),
    path('Registro/',Registro,name="Registro"),
    path('Registrar/',registrar,name="registrar"),
    path('Guardar/',guardarpost,name="guardarpost"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)