# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-18 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'MySubscriber', 'verbose_name_plural': 'A lot of Subscribers'},
        ),
    ]
