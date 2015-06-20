# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_login', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=100)),
                ('user_password', models.IntegerField()),
            ],
        ),
    ]
