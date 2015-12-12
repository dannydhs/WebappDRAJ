# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20151130_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produccion',
            old_name='valor_bruto_PInicial',
            new_name='valor_bruto_pinicial',
        ),
        migrations.RenameField(
            model_name='produccion',
            old_name='valorbruto_PFinal',
            new_name='valorbruto_pfinal',
        ),
    ]
