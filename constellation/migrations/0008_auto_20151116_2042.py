# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0007_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='jetsam',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='floatsam',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, always_update=True),
        ),
        migrations.AlterField(
            model_name='jetsam',
            name='maker',
            field=models.ForeignKey(to='constellation.Floatsam'),
        ),
        migrations.AlterField(
            model_name='jetsam',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, always_update=True),
        ),
    ]
