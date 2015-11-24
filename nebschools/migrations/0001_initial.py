# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_year', models.CharField(max_length=255)),
                ('actenglish', models.FloatField()),
                ('actmath', models.FloatField()),
                ('actreading', models.FloatField()),
                ('actscience', models.FloatField()),
                ('actcomposite', models.FloatField()),
                ('concatid', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CohortGrad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_year', models.CharField(max_length=255)),
                ('grad_pct', models.CharField(max_length=255)),
                ('concatid', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('agencykey', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('schoolid', models.CharField(max_length=255)),
                ('schoolname', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('dist_id', models.CharField(max_length=255)),
                ('state_acc', models.CharField(max_length=255)),
                ('nca_acc', models.CharField(max_length=255)),
                ('esu', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dropout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_year', models.CharField(max_length=255)),
                ('dropout_rate', models.FloatField()),
                ('concatid', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ELL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_year', models.CharField(max_length=255)),
                ('ellpct', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enrollment', models.IntegerField()),
                ('school_year', models.CharField(max_length=255)),
                ('concatid', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FedAcct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_year', models.CharField(max_length=255)),
                ('grade_tested', models.IntegerField()),
                ('year_testedstatus', models.CharField(max_length=255)),
                ('change', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FRL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FRLpct', models.FloatField()),
                ('concatid', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NESAscores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_year', models.CharField(max_length=255)),
                ('math_avg_score', models.FloatField()),
                ('math_basic_pct', models.FloatField()),
                ('math_proficent_pct', models.FloatField()),
                ('math_advanced_pct', models.FloatField()),
                ('math_not_tested', models.FloatField()),
                ('reading_avg_score', models.FloatField()),
                ('reading_basic_pct', models.FloatField()),
                ('reading_proficent_pct', models.FloatField()),
                ('reading_advanced_pct', models.FloatField()),
                ('reading_not_tested', models.FloatField()),
                ('science_avg_score', models.FloatField()),
                ('science_basic_pct', models.FloatField()),
                ('science_proficent_pct', models.FloatField()),
                ('science_advanced_pct', models.FloatField()),
                ('science_not_tested', models.FloatField()),
                ('writing_avg_score', models.FloatField()),
                ('writing_basic_pct', models.FloatField()),
                ('writing_proficent_pct', models.FloatField()),
                ('writing_advanced_pct', models.FloatField()),
                ('writing_not_tested', models.FloatField()),
                ('concat_join_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agencykey', models.CharField(max_length=255, db_index=True)),
                ('schoolid', models.CharField(max_length=255)),
                ('schoolname', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('dist_id', models.CharField(max_length=255)),
                ('state_acc', models.CharField(max_length=255)),
                ('nca_acc', models.CharField(max_length=255)),
                ('esu', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('district', models.ForeignKey(to='nebschools.District')),
            ],
        ),
        migrations.AddField(
            model_name='nesascores',
            name='agencykey',
            field=models.ForeignKey(to='nebschools.School'),
        ),
        migrations.AddField(
            model_name='frl',
            name='agencykey',
            field=models.ForeignKey(to='nebschools.School'),
        ),
        migrations.AddField(
            model_name='fedacct',
            name='agencykey',
            field=models.ForeignKey(to='nebschools.School'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='agencykey',
            field=models.ForeignKey(to='nebschools.School'),
        ),
        migrations.AddField(
            model_name='ell',
            name='agencykey',
            field=models.ForeignKey(to='nebschools.School'),
        ),
        migrations.AddField(
            model_name='dropout',
            name='agencykey',
            field=models.ForeignKey(to='nebschools.School'),
        ),
        migrations.AddField(
            model_name='cohortgrad',
            name='agencykey',
            field=models.ForeignKey(to='nebschools.School'),
        ),
        migrations.AddField(
            model_name='act',
            name='agencykey',
            field=models.ForeignKey(to='nebschools.School'),
        ),
    ]
