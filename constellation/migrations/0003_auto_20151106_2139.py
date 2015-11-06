# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0002_auto_20151106_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floatsam',
            name='peers',
        ),
        migrations.AddField(
            model_name='floatsam',
            name='coven',
            field=models.ManyToManyField(related_name='_floatsam_coven_+', to='constellation.Floatsam'),
        ),
    ]
