# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-07 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='client_phone',
            field=models.IntegerField(max_length=250, verbose_name='Numéro de téléphone du client'),
        ),
    ]
