# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0004_auto_20151115_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='floatsam',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='d', editable=False, unique=True, populate_from='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jetsam',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='d', editable=False, unique=True, populate_from='name'),
            preserve_default=False,
        ),
    ]
