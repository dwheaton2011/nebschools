# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebschools', '0002_auto_20151118_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='ditname',
            new_name='distname',
        ),
        migrations.AddField(
            model_name='district',
            name='distslug',
            field=models.SlugField(default='US/Central'),
            preserve_default=False,
        ),
    ]
