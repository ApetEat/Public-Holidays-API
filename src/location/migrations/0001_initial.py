# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-14 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Official code')),
                ('name', models.CharField(max_length=200, verbose_name='City')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Official code')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Official code')),
                ('name', models.CharField(max_length=100, verbose_name='Province')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Official code')),
                ('name', models.CharField(max_length=100, verbose_name='Region')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Country')),
            ],
            options={
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.AddField(
            model_name='province',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Region'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Province'),
        ),
    ]
