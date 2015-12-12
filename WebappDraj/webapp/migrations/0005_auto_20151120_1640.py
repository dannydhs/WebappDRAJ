# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20151110_0329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periodo_final',
            old_name='anio',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='periodo_inicial',
            old_name='anio',
            new_name='fecha',
        ),
        migrations.RemoveField(
            model_name='periodo_final',
            name='mes',
        ),
        migrations.RemoveField(
            model_name='periodo_inicial',
            name='mes',
        ),
    ]
