# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-22 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
    ]