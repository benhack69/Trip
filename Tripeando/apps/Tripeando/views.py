from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
from apps.Tripeando.models import Usuario,Rol,Post,Comentarios


# Create your views here.

def Inicio(request):
    return render(request,'Tripeando/index.html')

def Lugares(request):
    return render(request,'Tripeando/lugares.html')

def Blog(request):
    u = Usuario.objects.filter(usuario=request.user.username)
    posts= Post.objects.all()
    return render(request,'Tripeando/blog.html',{'posts':posts,'perfils':u})

def Crearpost(request):
    return render(request,'Tripeando/crearpost.html')

def Editarpost(request,id_post):
    instancia = Post.objects.get(id_post=id_post)
    return render(request,'Tripeando/editarpost.html',{'instancia':instancia})    

def Postvista(request):
    try:
        id_post = request.POST['id_post']
    except MultiValueDictKeyError: 
        id_post = False
        
    u = Usuario.objects.get(usuario=request.user.username)
    posts = Post.objects.filter(id_post=id_post)
    return render(request,'Tripeando/post.html',{'posts':posts,'perfils':u})

def Registro(request):
    return render(request,'Tripeando/registro.html')

def iniciar_sesion(request):
    return render(request,'Tripeando/login.html')
    

def Perfil(request):
    perfils = Usuario.objects.filter(usuario=request.user.username)
    return render(request,'Tripeando/perfil.html',{'perfils':perfils})

def Aperfil(request,usuario):
    instancia = Usuario.objects.get(usuario=usuario)
    return render(request,'Tripeando/editarperfil.html',{'instancia':instancia}) 

def Fperfil(request,usuario):
    instancia = Usuario.objects.get(usuario=usuario)
    return render(request,'Tripeando/editarfotop.html',{'instancia':instancia})      
   


#Registros
#Registrar Usuario
def registrar(request):
    usuario = request.POST['usuario']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    clave = request.POST['contrasena']
    image = request.FILES.get('foto')
    descripcion = request.POST['desc_perfil']
    rol = Rol.objects.get(nombre_rol = "Cliente")

    Usuario.objects.create(usuario=usuario,nombre=nombre,apellido=apellido,email=email,contrasena=clave,foto_perfil=image,desc_perfil=descripcion,rol=rol)
    user,created = User.objects.get_or_create(username=usuario)#cambiamos a una nueva forma
    user.set_password(clave)#seteamos la clave d euna manera diferente para que la reconozca con el encriptado correcto
    user.is_staff = True
    user.save()
    messages.success(request,'Se ha registrado exitosamente')
    return redirect('Registro')

def guardarpost(request):
    titulo = request.POST['titulo']
    desc_post = request.POST['desc_post']
    image = request.FILES.get('foto')
    now = datetime.now()

    posts = Usuario.objects.get(usuario=request.user.username)
    Post.objects.create(titulo=titulo,desc_post=desc_post,foto_post=image,visitas = 0,usuario2 = posts,fecha_publicacion=now)
    messages.success(request,'Se ha creado el post exitosamente')
    return redirect('Crearpost')

def guardarcomentario(request):
    desc_comentarios = request.POST['desc_comentarios']

    coments = Post.objects.get(usuario2=request.user.username)
    Comentarios.objects.create(desc_comentarios=desc_comentarios,post = coments)
    messages.success(request,'Comentario exitoso')
    return('Post')

def delete(request, id_post):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Post.objects.get(id_post=id_post)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('Blog')


def edit(request, id_post):
    titulo = request.POST['titulo']
    desc_post = request.POST['desc_post']
    #image = request.FILES.get('foto')

    instancia = Post.objects.filter(id_post=id_post)
    instancia.update(titulo=titulo,desc_post=desc_post)
    messages.success(request,'Editado Correctamente')
    return redirect('Blog')

def editarperfil(request,usuario):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    desc_perfil = request.POST['desc_perfil']
    #image = request.FILES.get('foto')

    instancia = Usuario.objects.filter(usuario=usuario)
    instancia.update(nombre=nombre,apellido=apellido,desc_perfil=desc_perfil)
    return redirect('Perfil')

def editarperfilfoto(request,usuario):
    image = request.FILES.get('foto')

    instancia = Usuario.objects.filter(usuario=usuario)
    instancia.update(foto_perfil=image)
    instancia.save()
    return redirect('Perfil')    
