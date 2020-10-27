from django.contrib import admin
from django.urls import path,include
from .views import Inicio,Lugares,Blog,Crearpost,Login,Perfil,Post,Registro

urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('lugares/',Lugares,name="Lugares"),
    path('blog/',Blog,name="Blog"),
    path('crearpost/',Crearpost,name="Crearpost"),
    path('login/',Login,name="Login"),
    path('perfil/',Perfil,name="Perfil"),
    path('post/',Post,name="Post"),
    path('registro/',Registro,name="Registro"),
]