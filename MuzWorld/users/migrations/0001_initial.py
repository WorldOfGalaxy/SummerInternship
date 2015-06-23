# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('audio_singer', models.CharField(max_length=50)),
                ('audio_name', models.CharField(max_length=50)),
                ('audio_track', models.FileField(upload_to='/audio')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comment_context', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name_of_genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, parent_link=True, primary_key=True, auto_created=True)),
                ('user_image', models.ImageField(height_field=200, width_field=100, upload_to='/photos')),
                ('user_genre', models.ForeignKey(to='users.Genre')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('point_maker', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('point_to_audio', models.ForeignKey(to='users.Audio')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_to',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_to_audio',
            field=models.ForeignKey(to='users.Audio'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_writer',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='writer'),
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_genre',
            field=models.ForeignKey(to='users.Genre'),
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
