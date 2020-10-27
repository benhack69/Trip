from django.contrib import admin
from apps.Tripeando.models import Rol,Usuario,RRSS,Usuario_RRSS,Post,Comentarios,Respuesta_Comentarios,Lugares

# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(RRSS)
admin.site.register(Usuario_RRSS)
admin.site.register(Post)
admin.site.register(Comentarios)
admin.site.register(Respuesta_Comentarios)
admin.site.register(Lugares)