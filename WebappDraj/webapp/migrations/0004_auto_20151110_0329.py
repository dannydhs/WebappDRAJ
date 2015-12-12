# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20151016_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo_final',
            name='valor_bruto',
            field=models.DecimalField(max_digits=5, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='periodo_inicial',
            name='valor_bruto',
            field=models.DecimalField(max_digits=5, decimal_places=3),
        ),
    ]
