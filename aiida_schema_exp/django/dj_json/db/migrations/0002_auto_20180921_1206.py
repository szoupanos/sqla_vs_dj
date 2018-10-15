# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 12:06
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbnode',
            name='jattributes',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=None),
        ),
        migrations.AddField(
            model_name='dbnode',
            name='jextras',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=None),
        ),
        migrations.AlterField(
            model_name='dbuser',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='dbuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='dbuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
