# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebschools', '0007_auto_20151119_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohortgrad',
            name='grad_pct',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dropout',
            name='dropout_rate',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ell',
            name='ellpct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='frl',
            name='FRLpct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='math_advanced_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='math_avg_score',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='math_basic_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='math_not_tested',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='math_proficent_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='reading_advanced_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='reading_avg_score',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='reading_basic_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='reading_not_tested',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='reading_proficent_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='science_advanced_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='science_avg_score',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='science_basic_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='science_not_tested',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='science_proficent_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='writing_advanced_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='writing_avg_score',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='writing_basic_pct',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='writing_not_tested',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nesascores',
            name='writing_proficent_pct',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
