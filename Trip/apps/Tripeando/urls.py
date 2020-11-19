from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from .views import Inicio,Lugares,Blog,Crearpost,Editarpost,Perfil,Postvista,Registro,recuperacion_cuenta,iniciar_sesion,registrar,formulario_recuperacion,guardarpost,guardarcomentario,delete,edit,editarperfil,editarperfilfoto,Aperfil,Fperfil,formulario_cambiar_contrasena,pregunta_seguridad,cambiocontra,Tusposts,CrearComentario,UsuarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios/',UsuarioViewSet)

urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('lugares/',Lugares,name="Lugares"),
    path('blog/',Blog,name="Blog"),
    path('crearpost/',Crearpost,name="Crearpost"),
    path('crearcomentario/',CrearComentario,name="Crearcomentario"),
    path('tusposts/',Tusposts,name="tusposts"),
    path('editarpost/<int:id_post>',Editarpost, name='editarpost'),
    path('Aperfil/<str:usuario>',Aperfil, name='Aperfil'),
    path('Fperfil/<str:usuario>',Fperfil, name='Fperfil'),
    path('login/',LoginView.as_view(template_name='Tripeando/login.html'),name="iniciar_sesion"),
    path('logout/',LogoutView.as_view(template_name='Tripeando/index.html'),name="logout"),
    path('perfil/',Perfil,name="Perfil"),
    path('post/',Postvista,name="Post"),
    path('Registro/',Registro,name="Registro"),
    path('recuperacioncontra/',recuperacion_cuenta,name="recuperacioncontra"),
    path('formulario_recuperacion/',formulario_recuperacion,name="formulario_recuperacion"),
    path('formulario_cambiar_contrasena/',formulario_cambiar_contrasena,name="formulario_cambiar_contrasena"),
    path('cambiocontra/',cambiocontra,name="cambiocontra"),
    path('pregunta_seguridad/',pregunta_seguridad,name="pregunta_seguridad"),
    path('Registrar/',registrar,name="registrar"),
    path('Guardar/',guardarpost,name="guardarpost"),
    path('Guardarcomentario/',guardarcomentario,name="guardarcomentario"),
    path('delete/<int:id_post>', delete),
    path('edit/<int:id_post>', edit),
    path('editarperfil/<str:usuario>', editarperfil),
    path('editarperfilfoto/<str:usuario>', editarperfilfoto),
    path('api/',include(router.urls)),
    path('oauth/',include('social_django.urls',namespace='social')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)