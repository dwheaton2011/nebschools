# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebschools', '0005_remove_school_schoolid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='actcomposite',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='act',
            name='actenglish',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='act',
            name='actmath',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='act',
            name='actreading',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='act',
            name='actscience',
            field=models.FloatField(blank=True),
        ),
    ]
