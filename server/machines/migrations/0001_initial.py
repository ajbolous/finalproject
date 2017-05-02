# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('serial', models.CharField(max_length=50)),
                ('weight', models.IntegerField(null=True)),
                ('speed', models.IntegerField(null=True)),
                ('capacity', models.IntegerField(null=True)),
                ('weightCapacity', models.IntegerField(null=True)),
                ('fuelCapacity', models.IntegerField(null=True)),
                ('fuelConsumption', models.IntegerField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('isAvailable', models.BooleanField()),
                ('fuelLevel', models.FloatField(null=True)),
                ('modalYear', models.IntegerField(null=True)),
            ],
        ),
    ]
