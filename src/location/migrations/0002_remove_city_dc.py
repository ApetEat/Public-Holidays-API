# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-14 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='dc',
        ),
    ]
