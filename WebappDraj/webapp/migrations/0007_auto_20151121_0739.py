# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20151121_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='periodo',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='valor',
            field=models.DecimalField(max_digits=8, decimal_places=5),
        ),
    ]
