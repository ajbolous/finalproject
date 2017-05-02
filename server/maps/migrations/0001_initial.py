# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
                ('material', models.CharField(max_length=50)),
                ('capacity', models.FloatField()),
            ],
        ),
    ]
