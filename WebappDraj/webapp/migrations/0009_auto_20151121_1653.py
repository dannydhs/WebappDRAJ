# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20151121_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produccion_periodo_final',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.DecimalField(max_digits=8, decimal_places=5)),
                ('anio', models.CharField(max_length=4, null=True, blank=True)),
                ('mes', models.CharField(max_length=2, null=True, blank=True)),
                ('producto', models.ForeignKey(blank=True, to='webapp.Producto', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produccion_periodo_inicial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.DecimalField(max_digits=8, decimal_places=5)),
                ('anio', models.CharField(max_length=4, null=True, blank=True)),
                ('mes', models.CharField(max_length=2, null=True, blank=True)),
                ('producto', models.ForeignKey(blank=True, to='webapp.Producto', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produccion_resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('variacion', models.DecimalField(max_digits=8, decimal_places=5)),
                ('indice_cantidad', models.DecimalField(max_digits=8, decimal_places=5)),
                ('produccion_periodo_final', models.ForeignKey(blank=True, to='webapp.Produccion_periodo_final', null=True)),
                ('produccion_periodo_inicial', models.ForeignKey(blank=True, to='webapp.Produccion_periodo_inicial', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='produccion',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Produccion',
        ),
    ]
