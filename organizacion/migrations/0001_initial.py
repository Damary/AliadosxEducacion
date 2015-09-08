# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aldea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(help_text='Codigo Oficial de la aldea', max_length=3)),
                ('nombre', models.CharField(help_text='Nombre de la Aldea', max_length=128)),
            ],
            options={
                'verbose_name': 'Aldea',
                'verbose_name_plural': 'Aldeas',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_categoria', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(help_text='Codigo Oficial del Departamento', unique=True, max_length=2)),
                ('nombre', models.CharField(help_text=b'Nombre del Departamento', unique=True, max_length=128)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(help_text='Codigo Oficial del municipio en el departamento', max_length=2)),
                ('nombre', models.CharField(help_text=b'Nombre del Municipio', max_length=128)),
                ('departamento', models.ForeignKey(help_text=b'Departamento en el cual se encuentra ubicado', to='organizacion.Departamento')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rtn', models.CharField(help_text='Ingrese el RTN de la Organizacion', unique=True, max_length=200)),
                ('razon_social', models.CharField(help_text='Ingrese la Razoo Social de la Organizacion', max_length=200)),
                ('nombre_comercial', models.CharField(help_text='Ingrese el Nombre Comercial de la Organizacion', max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('correo_electronico', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PresupuestoDonacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto_total', models.PositiveSmallIntegerField(help_text=b'Monto Total de la Donacion')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('categoria', models.ForeignKey(to='organizacion.Categoria')),
                ('organizacion', models.ForeignKey(to='organizacion.Organizacion')),
                ('usuario_creador', models.ForeignKey(related_name='r_inasistencia_creador', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('usuario_modifico', models.ForeignKey(related_name='r_inasistencia_modificador', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(help_text='Ingrese el Rubro de la Organizacion', max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(help_text='Ingrese el sector (Gobierno, Privada, ONG) de la Organizacion', max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sub_categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_sub_categoria', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('area', models.ForeignKey(to='organizacion.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion_completa', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('aldea', models.ForeignKey(to='organizacion.Aldea')),
                ('departamento', models.ForeignKey(to='organizacion.Departamento')),
                ('municipio', models.ForeignKey(to='organizacion.Municipio')),
                ('organizacion', models.ForeignKey(to='organizacion.Organizacion')),
            ],
        ),
        migrations.AddField(
            model_name='organizacion',
            name='rubro',
            field=models.ForeignKey(to='organizacion.Rubro'),
        ),
        migrations.AddField(
            model_name='organizacion',
            name='sector',
            field=models.ForeignKey(to='organizacion.Sector'),
        ),
        migrations.AddField(
            model_name='aldea',
            name='municipio',
            field=models.ForeignKey(help_text='Municipio donde se encuentra ubicada la aldea', to='organizacion.Municipio'),
        ),
        migrations.AlterUniqueTogether(
            name='municipio',
            unique_together=set([('codigo', 'departamento')]),
        ),
    ]
