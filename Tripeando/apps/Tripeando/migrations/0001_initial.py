# Generated by Django 3.1.2 on 2020-10-29 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id_comentarios', models.IntegerField(primary_key=True, serialize=False)),
                ('desc_comentarios', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lugares',
            fields=[
                ('id_lugares', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_lugar', models.CharField(max_length=40)),
                ('foto_lugares', models.ImageField(upload_to='uploads')),
                ('desc_lugares', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='RRSS',
            fields=[
                ('id_rs', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_rs', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('contrasena', models.CharField(max_length=30)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('desc_perfil', models.CharField(blank=True, max_length=50, null=True)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tripeando.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_RRSS',
            fields=[
                ('id_usuario_rrss', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('rrss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tripeando.rrss')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tripeando.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta_Comentarios',
            fields=[
                ('id_respuesta_c', models.IntegerField(primary_key=True, serialize=False)),
                ('r_comentario', models.CharField(max_length=100, null=True)),
                ('comentarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tripeando.comentarios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tripeando.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('desc_post', models.CharField(max_length=150)),
                ('foto_post', models.ImageField(upload_to='uploads')),
                ('fecha_publicacion', models.DateField()),
                ('visitas', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tripeando.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='comentarios',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tripeando.post'),
        ),
    ]
