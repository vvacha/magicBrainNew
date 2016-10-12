# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('lesson_name', models.CharField(max_length=200)),
                ('lesson_text', models.TextField()),
                ('lesson_creator', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'lesson',
            },
        ),
    ]
