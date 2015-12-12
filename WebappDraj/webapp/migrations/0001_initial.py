# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo_final',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.DateField()),
                ('mes', models.DateField()),
                ('valor_bruto', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo_inicial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.DateField()),
                ('mes', models.DateField()),
                ('valor_bruto', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_sector',
            fields=[
                ('idsubsector', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('variacion', models.DecimalField(max_digits=5, decimal_places=2)),
                ('ind_cant', models.DecimalField(max_digits=5, decimal_places=2)),
                ('pfinal', models.ForeignKey(to='webapp.Periodo_final')),
                ('pinicial', models.ForeignKey(to='webapp.Periodo_inicial')),
            ],
        ),
        migrations.AddField(
            model_name='sector',
            name='sbsector',
            field=models.ForeignKey(to='webapp.Sub_sector'),
        ),
    ]
