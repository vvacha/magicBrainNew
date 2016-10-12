# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0002_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(upload_to='avatar/', null=True, default='/media/NoAvatar/No_avatar.jpg', blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sity',
            field=models.CharField(max_length=50, null=True, default='No_city', blank=True),
        ),
    ]
