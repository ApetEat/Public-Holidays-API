# Generated by Django 2.0.2 on 2018-02-08 10:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

from ..sql.sqldataloaders import (country_data, community_data,
                                  province_data, locality_data)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='Official code')),
                ('name', models.CharField(max_length=100, verbose_name='Community')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name_plural': 'Communities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Official code')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Country')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Official code')),
                ('name', models.CharField(max_length=200, verbose_name='Locality')),
                ('dc', models.IntegerField(blank=True, verbose_name='Control Digit')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name_plural': 'Localities',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='Official code')),
                ('name', models.CharField(max_length=100, verbose_name='Province')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicholidays.Community')),
            ],
        ),
        migrations.AddField(
            model_name='locality',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicholidays.Province'),
        ),
        migrations.AddField(
            model_name='community',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicholidays.Country'),
        ),
        migrations.RunPython(country_data),
        migrations.RunPython(community_data),
        migrations.RunPython(province_data),
        migrations.RunPython(locality_data),
    ]
