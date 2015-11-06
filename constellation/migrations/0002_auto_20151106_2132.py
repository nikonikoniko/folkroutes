# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='constellation',
            name='story',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='story',
            field=models.TextField(blank=True, null=True),
        ),
    ]
