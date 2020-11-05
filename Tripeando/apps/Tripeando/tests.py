from django.test import TestCase
from apps.Tripeando.models import Rol,RRSS,Usuario

# Create your tests here.
class RolTestCase(TestCase):
    def setUp(self):
        Rol.objects.create(id_rol_usuario=3,nombre_rol="admin")
        Rol.objects.create(id_rol_usuario=4,nombre_rol="usuario")

    def test_rol(self):
        dato1= Rol.objects.get(id_rol_usuario=3)
        dato2= Rol.objects.get(id_rol_usuario=4)

        self.assertEquals(dato1.nombre_rol,'admin')
        self.assertEquals(dato2.nombre_rol,'usuario')

class RRSSTestCase(TestCase):
    def setUp(self):
        RRSS.objects.create(id_rs=1,nombre_rs="facebook")
        RRSS.objects.create(id_rs=2,nombre_rs="instagram")

    def test_rrss(self):
        dato1=RRSS.objects.get(id_rs=1)
        dato2=RRSS.objects.get(id_rs=2)

        self.assertEquals(dato1.nombre_rs,'facebook')
        self.assertEquals(dato2.nombre_rs,'instagram')

class UsuarioTestCase(TestCase):
    def setUp(self):
        Rol.objects.create(id_rol_usuario=4,nombre_rol="admin_x")
        r = Rol.objects.get(nombre_rol = "admin_x")
        Usuario.objects.create(usuario="naruto",nombre="naruto",apellido="uzumaki",email="naruto@gmail.com",contrasena="narutouzumaki",foto_perfil="ola.png",desc_perfil="mi camino ninja",rol=r)
        Usuario.objects.create(usuario="sasuke",nombre="sasuke",apellido="uchiha",email="sasuke@gmail.com",contrasena="sasukeuchiha",foto_perfil="chao.png",desc_perfil="soy un vengador",rol=r)

    def test_usuario(self):
        dato1= Usuario.objects.get(desc_perfil="mi camino ninja")
        dato2= Usuario.objects.get(desc_perfil="soy un vengador")

        self.assertEquals(dato1.usuario,'naruto')
        self.assertEquals(dato2.usuario,'sasuke')