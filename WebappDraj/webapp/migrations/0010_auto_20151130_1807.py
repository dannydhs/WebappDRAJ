# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20151121_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_bruto_PInicial', models.DecimalField(max_digits=8, decimal_places=5)),
                ('periodo_inicial_anio', models.CharField(max_length=4, null=True, blank=True)),
                ('periodo_inicial_mes', models.CharField(max_length=2, null=True, blank=True)),
                ('valorbruto_PFinal', models.DecimalField(max_digits=8, decimal_places=5)),
                ('periodo_final_anio', models.CharField(max_length=4, null=True, blank=True)),
                ('periodo_final_mes', models.CharField(max_length=2, null=True, blank=True)),
                ('variacion', models.DecimalField(max_digits=8, decimal_places=5)),
                ('indice_cantidad', models.DecimalField(max_digits=8, decimal_places=5)),
                ('producto', models.ForeignKey(blank=True, to='webapp.Producto', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subsector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('sector', models.ForeignKey(blank=True, to='webapp.Sector', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='produccion_periodo_final',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='produccion_periodo_inicial',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='produccion_resultado',
            name='produccion_periodo_final',
        ),
        migrations.RemoveField(
            model_name='produccion_resultado',
            name='produccion_periodo_inicial',
        ),
        migrations.DeleteModel(
            name='Produccion_periodo_final',
        ),
        migrations.DeleteModel(
            name='Produccion_periodo_inicial',
        ),
        migrations.DeleteModel(
            name='Produccion_resultado',
        ),
        migrations.AddField(
            model_name='producto',
            name='subsector',
            field=models.ForeignKey(blank=True, to='webapp.Subsector', null=True),
        ),
    ]
