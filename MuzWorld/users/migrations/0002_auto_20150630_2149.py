# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musician',
            options={},
        ),
        migrations.AlterModelManagers(
            name='musician',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='musician',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='musician',
            name='id',
            field=models.AutoField(verbose_name='ID', auto_created=True, default=datetime.datetime(2015, 6, 30, 18, 49, 0, 281405, tzinfo=utc), primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musician',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='musician',
            name='user_genre',
            field=models.ForeignKey(blank=True, to='users.Genre'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='user_image',
            field=models.ImageField(width_field=100, blank=True, upload_to='/photos', height_field=200),
        ),
    ]
