# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_field_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='degree',
            field=models.CharField(choices=[('M', 'Master'), ('P', 'PHD')], default='P', max_length=1),
            preserve_default=False,
        ),
    ]