# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20151015_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='sub_sector',
            name='producto',
            field=models.ForeignKey(blank=True, to='webapp.Productos', null=True),
        ),
    ]
