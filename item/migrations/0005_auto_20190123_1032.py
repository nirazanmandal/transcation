# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-23 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20190118_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='iname',
        ),
    ]
