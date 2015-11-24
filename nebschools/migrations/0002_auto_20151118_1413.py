# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebschools', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='schoolid',
            new_name='distid',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='schoolname',
            new_name='ditname',
        ),
    ]
