# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 23:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_program_degree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='minimum_gre',
        ),
    ]