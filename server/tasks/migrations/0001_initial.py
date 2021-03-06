# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lName', models.CharField(max_length=50)),
                ('lType', models.CharField(max_length=50)),
                ('lLong', models.FloatField()),
                ('lLate', models.FloatField()),
                ('lMaterial', models.CharField(max_length=50)),
                ('lCapacity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sDescription', models.CharField(max_length=200)),
                ('sType', models.CharField(max_length=50)),
                ('sStartDate', models.DateField()),
                ('sFinishDate', models.DateField()),
                ('sCapacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tName', models.CharField(max_length=50)),
                ('tDescription', models.CharField(max_length=200)),
                ('tSite', models.CharField(max_length=50)),
                ('tPriority', models.IntegerField()),
                ('tDeadline', models.DateField()),
                ('tStartDate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='subtask',
            name='sTask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
    ]
