# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seconduser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floatsam',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('website', models.CharField(null=True, blank=True, max_length=255)),
                ('story', models.TextField(null=True, blank=True)),
                ('floatsam_id', models.AutoField(serialize=False, primary_key=True)),
                ('geom', djgeojson.fields.PointField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jetsam',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('website', models.CharField(null=True, blank=True, max_length=255)),
                ('story', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Constellation',
            fields=[
                ('floatsam_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='constellation.Floatsam')),
            ],
            options={
                'abstract': False,
            },
            bases=('constellation.floatsam',),
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('floatsam_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='constellation.Floatsam')),
                ('seconduser_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='seconduser.SecondUser')),
            ],
            options={
                'abstract': False,
            },
            bases=('seconduser.seconduser', 'constellation.floatsam'),
        ),
        migrations.AddField(
            model_name='jetsam',
            name='maker',
            field=models.ForeignKey(to='constellation.Floatsam'),
        ),
        migrations.AddField(
            model_name='floatsam',
            name='coven',
            field=models.ManyToManyField(related_name='_floatsam_coven_+', to='constellation.Floatsam'),
        ),
    ]
