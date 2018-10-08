# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 07:36
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturierApp', '0003_auto_20181005_0857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devis',
            options={'verbose_name_plural': 'Devis'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='full_name', unique=True),
        ),
    ]
