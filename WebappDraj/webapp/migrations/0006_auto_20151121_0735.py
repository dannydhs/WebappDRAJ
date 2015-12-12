# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20151120_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.DecimalField(max_digits=5, decimal_places=2)),
                ('periodo', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30, null=True, blank=True)),
                ('produccion', models.ForeignKey(blank=True, to='webapp.Produccion', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sector',
            name='sbsector',
        ),
        migrations.RemoveField(
            model_name='sub_sector',
            name='pfinal',
        ),
        migrations.RemoveField(
            model_name='sub_sector',
            name='pinicial',
        ),
        migrations.RemoveField(
            model_name='sub_sector',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Periodo_final',
        ),
        migrations.DeleteModel(
            name='Periodo_inicial',
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
        migrations.DeleteModel(
            name='Sub_sector',
        ),
    ]
