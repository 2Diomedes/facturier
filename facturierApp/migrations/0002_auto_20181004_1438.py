# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-04 14:38
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('facturierApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
