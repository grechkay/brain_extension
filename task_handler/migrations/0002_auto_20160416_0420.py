# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_handler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeadlineComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=120)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_handler.DeadlineTask')),
            ],
        ),
        migrations.CreateModel(
            name='RecurringComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=120)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecurringEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=120)),
                ('completed_time', models.DateTimeField(auto_now=True)),
                ('time_since_last', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_handler.RecurringTask')),
            ],
        ),
        migrations.AddField(
            model_name='recurringcomment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_handler.RecurringEvent'),
        ),
    ]
