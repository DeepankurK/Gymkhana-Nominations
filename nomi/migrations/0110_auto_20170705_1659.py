# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0109_remove_nomination_club_search'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nomination',
            old_name='closing_date',
            new_name='deadline',
        ),
    ]
