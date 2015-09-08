# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('area', models.ForeignKey(to='organizacion.Categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='sub_categoria',
            name='area',
        ),
        migrations.DeleteModel(
            name='sub_categoria',
        ),
    ]
