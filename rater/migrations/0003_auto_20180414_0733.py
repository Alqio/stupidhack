# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-14 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0002_ratemandarin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratemandarin',
            name='nroOfRate',
            field=models.IntegerField(default=0),
        ),
    ]