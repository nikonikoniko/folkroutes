# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import folkroutes.current_user
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0005_auto_20151115_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='jetsam',
            name='type',
            field=models.IntegerField(choices=[(1, 'Writing'), (2, 'Audio'), (3, 'Image'), (4, 'Document')], default=1),
        ),
        migrations.AddField(
            model_name='jetsam',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='jetsam'),
        ),
        migrations.AlterField(
            model_name='floatsam',
            name='coven',
            field=models.ManyToManyField(blank=True, to='constellation.Floatsam', related_name='_floatsam_coven_+'),
        ),
        migrations.AlterField(
            model_name='floatsam',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, always_update=True, editable=False, populate_from='name'),
        ),
        migrations.AlterField(
            model_name='jetsam',
            name='maker',
            field=models.ForeignKey(default=folkroutes.current_user.get_current_user, to='constellation.Floatsam'),
        ),
        migrations.AlterField(
            model_name='jetsam',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, always_update=True, editable=False, populate_from='name'),
        ),
    ]
