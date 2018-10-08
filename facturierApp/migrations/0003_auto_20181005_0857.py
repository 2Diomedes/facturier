# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 08:57
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('facturierApp', '0002_auto_20181004_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('validated_at', models.DateTimeField(auto_now=True, verbose_name='Date de validation')),
                ('payment', models.CharField(choices=[('CASH', 'cash'), ('CARD', 'card'), ('CHECK', 'check'), ('PAYPAL', 'paypal'), ('BITCOIN', 'bitcoin')], default='CASH', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=['first_name', 'last_name'])),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='LigneBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('devis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturierApp.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='LigneDevis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='facture',
            name='client',
        ),
        migrations.RemoveField(
            model_name='facture',
            name='listProduit',
        ),
        migrations.RemoveField(
            model_name='lignecmd',
            name='produit',
        ),
        migrations.RenameField(
            model_name='devis',
            old_name='dateCreation',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='devis',
            old_name='dateValid',
            new_name='validated_at',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='client',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='listProduit',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Facture',
        ),
        migrations.DeleteModel(
            name='LigneCmd',
        ),
        migrations.DeleteModel(
            name='Produit',
        ),
        migrations.AddField(
            model_name='lignedevis',
            name='devis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturierApp.Devis'),
        ),
        migrations.AddField(
            model_name='lignedevis',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturierApp.Product'),
        ),
        migrations.AddField(
            model_name='lignebill',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturierApp.Product'),
        ),
        migrations.AddField(
            model_name='bill',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturierApp.Customer'),
        ),
        migrations.AddField(
            model_name='devis',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturierApp.Customer'),
        ),
    ]