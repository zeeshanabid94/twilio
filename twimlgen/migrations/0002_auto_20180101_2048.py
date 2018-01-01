# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-01 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twimlgen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fizzbuzz', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='call',
            name='origin_time',
        ),
        migrations.AddField(
            model_name='game',
            name='call',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='twimlgen.Call'),
        ),
    ]
