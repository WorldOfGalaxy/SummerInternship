# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('audio_singer', models.CharField(max_length=50)),
                ('audio_name', models.CharField(max_length=50)),
                ('audio_track', models.FileField(upload_to='/audio')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('comment_context', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, verbose_name='date published')),
                ('comment_to', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('comment_to_audio', models.ForeignKey(to='users.Audio')),
                ('comment_writer', models.OneToOneField(related_name='writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name_of_genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('user_image', models.ImageField(upload_to='/photos', width_field=100, blank=True, height_field=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user_genre', models.ForeignKey(to='users.Genre', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('value', models.IntegerField(default=0)),
                ('point_maker', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('point_to_audio', models.ForeignKey(to='users.Audio')),
            ],
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
