from django.shortcuts import render

# Create your views here.

def Inicio(request):
    return render(request,'Tripeando/index.html')

def Lugares(request):
    return render(request,'Tripeando/lugares.html')

def Blog(request):
    return render(request,'Tripeando/blog.html')

def Crearpost(request):
    return render(request,'Tripeando/crearpost.html')

def Login(request):
    return render(request,'Tripeando/login.html')

def Perfil(request):
    return render(request,'Tripeando/perfil.html')

def Post(request):
    return render(request,'Tripeando/post.html')

def Registro(request):
    return render(request,'Tripeando/registro.html')