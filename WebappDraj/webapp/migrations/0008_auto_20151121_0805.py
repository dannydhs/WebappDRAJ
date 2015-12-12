# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20151121_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='produccion',
        ),
        migrations.AddField(
            model_name='produccion',
            name='producto',
            field=models.ForeignKey(blank=True, to='webapp.Producto', null=True),
        ),
    ]
