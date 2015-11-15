# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='vanity_image',
            field=stdimage.models.StdImageField(upload_to='vanity_image', blank=True),
        ),
    ]
