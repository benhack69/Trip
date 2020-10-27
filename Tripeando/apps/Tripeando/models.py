from django.db import models

# Create your models here.

class Rol(models.Model):
    id_rol_usuario = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=14)

class Usuario(models.Model):
    usuario = models.CharField(max_length=20,null=False,blank=False)
    nombre = models.CharField(max_length=20,null=False,blank=False)
    apellido = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField(primary_key=True,max_length=50,null=False,blank=False)
    contrasena = models.CharField(max_length=30,null=False,blank=False)
    foto_perfil = models.ImageField(null=True,blank=True)
    desc_perfil = models.CharField(max_length=50,null=True,blank=True)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

class RRSS(models.Model):
    id_rs = models.IntegerField(primary_key=True)
    nombre_rs = models.CharField(max_length=15,null=True,blank=True)

class Usuario_RRSS(models.Model):
    id_usuario_rrss = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=100,null=True,blank=True)
    rrss = models.ForeignKey(RRSS,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Post(models.Model):
    id_post = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50,null=False,blank=False) 
    desc_post = models.CharField(max_length=150,null=False,blank=False)
    foto_post = models.ImageField(null=False,blank=False)
    fecha_publicacion = models.DateField()
    visitas = models.IntegerField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)


class Comentarios(models.Model):
    id_comentarios = models.IntegerField(primary_key=True)
    desc_comentarios = models.CharField(max_length=100,null=True,blank=False)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

class Respuesta_Comentarios(models.Model):
    id_respuesta_c = models.IntegerField(primary_key=True)
    r_comentario = models.CharField(max_length=100,null=True,blank=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    comentarios = models.ForeignKey(Comentarios,on_delete=models.CASCADE)

class Lugares(models.Model):
    id_lugares = models.IntegerField(primary_key=True)
    nombre_lugar = models.CharField(max_length=40,null=False,blank=False)
    foto_lugares = models.ImageField()
    desc_lugares = models.CharField(max_length=200,null=False,blank=False)
    status = models.IntegerField()



