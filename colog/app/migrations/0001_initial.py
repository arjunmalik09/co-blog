# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUserprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField()),
                ('mobile_no', models.CharField(unique=True, max_length=20)),
                ('education_place', models.CharField(max_length=40)),
                ('education_field', models.CharField(max_length=40)),
                ('employment_place', models.CharField(max_length=40)),
                ('employment_designation', models.CharField(max_length=40)),
                ('occupation', models.CharField(max_length=40)),
                ('residence_place', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=30)),
                ('picture', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'app_userprofile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('c_id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('likes', models.IntegerField()),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('f_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'follows',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HasInterest',
            fields=[
                ('h_i_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'has_interest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HasTags',
            fields=[
                ('h_t_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'has_tags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('pt_id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('likes', models.IntegerField()),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('t_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'topic',
                'managed': False,
            },
        ),
    ]
