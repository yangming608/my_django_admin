# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-07 02:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='UserInfo',
        ),
    ]
