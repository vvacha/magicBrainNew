# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_lesson_lesson_immage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson_immage',
            new_name='lesson_image',
        ),
    ]
