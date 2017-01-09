# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 00:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20161220_2250'),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateField(default='11/07/2017'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='time',
            field=models.TimeField(default='18:57'),
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='user',
        ),
        migrations.AddField(
            model_name='appointments',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
            preserve_default=False,
        ),
    ]
