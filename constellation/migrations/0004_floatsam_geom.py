# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0003_auto_20151106_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='floatsam',
            name='geom',
            field=djgeojson.fields.PointField(null=True, blank=True),
        ),
    ]
