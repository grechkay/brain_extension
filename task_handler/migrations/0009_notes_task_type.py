# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_handler', '0008_auto_20160419_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='task_type',
            field=models.CharField(default='note', max_length=120),
        ),
    ]