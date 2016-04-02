# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0008_auto_20151116_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionRequest',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('initiator', models.ForeignKey(to='constellation.Floatsam', related_name='initiator')),
                ('recipient', models.ForeignKey(to='constellation.Floatsam', related_name='recipient')),
            ],
        ),
    ]
