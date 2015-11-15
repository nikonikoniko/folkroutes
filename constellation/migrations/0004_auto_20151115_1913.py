# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0003_constellation_vanity_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constellation',
            name='vanity_image',
        ),
        migrations.RemoveField(
            model_name='star',
            name='vanity_image',
        ),
        migrations.AddField(
            model_name='floatsam',
            name='vanity_image',
            field=stdimage.models.StdImageField(upload_to='vanity_image', blank=True),
        ),
    ]
