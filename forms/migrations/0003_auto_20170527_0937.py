# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20170526_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
