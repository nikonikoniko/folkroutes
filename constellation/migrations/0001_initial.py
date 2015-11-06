# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seconduser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floatsam',
            fields=[
                ('floatsam_id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Constellation',
            fields=[
                ('floatsam_ptr', models.OneToOneField(auto_created=True, to='constellation.Floatsam', serialize=False, parent_link=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('constellation.floatsam', models.Model),
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('floatsam_ptr', models.OneToOneField(auto_created=True, to='constellation.Floatsam', parent_link=True)),
                ('seconduser_ptr', models.OneToOneField(auto_created=True, to='seconduser.SecondUser', serialize=False, parent_link=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('seconduser.seconduser', 'constellation.floatsam', models.Model),
        ),
        migrations.AddField(
            model_name='floatsam',
            name='peers',
            field=models.ManyToManyField(related_name='_floatsam_peers_+', to='constellation.Floatsam'),
        ),
    ]
