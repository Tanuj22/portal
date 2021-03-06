# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-03-16 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0012_requestcommunity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestcommunity',
            name='type_community',
            field=models.CharField(choices=[('Affinity Group', 'Affinity Group (Latinas in Computing, LGBT, etc)'), ('Special Interest Group', 'Special Interest Group (Student Researchers, Systers in Government,Women in Cyber Security, etc) '), ('Email list', 'Email list (using Mailman3)'), ('Other', 'Other')], default=None, max_length=255, verbose_name='Type of Community'),
        ),
    ]
