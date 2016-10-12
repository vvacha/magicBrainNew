# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0003_auto_20160913_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='sity',
            new_name='city',
        ),
    ]
