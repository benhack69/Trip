# Generated by Django 3.1.2 on 2020-11-09 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tripeando', '0008_auto_20201105_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario_rrss',
            name='rrss',
        ),
        migrations.RemoveField(
            model_name='usuario_rrss',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='RRSS',
        ),
        migrations.DeleteModel(
            name='Usuario_RRSS',
        ),
    ]
