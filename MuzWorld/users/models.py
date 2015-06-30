import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Genre(models.Model):
	name_of_genre = models.CharField(max_length = 50)
	def __str__(self):
		return self.name_of_genre

class Musician(models.Model):
	user = models.ForeignKey(User, default = None)
	user_image = models.ImageField(upload_to = '/photos', height_field = 200, width_field = 100, max_length=100, blank = True)
	user_genre = models.ForeignKey(Genre, blank = True)
	def __str__(self):
		return self.user_name
	
class Audio(models.Model):
	audio_owner = models.ForeignKey(User)
	audio_singer = models.CharField(max_length = 50)
	audio_name = models.CharField(max_length = 50)
	audio_track = models.FileField(upload_to = '/audio')
	audio_genre = models.ForeignKey(Genre)
	def __str__(self):
		return self.audio_name


class Comment(models.Model):
	comment_writer = models.OneToOneField(User,related_name = 'writer')
	comment_context = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published', blank = True)
	comment_to = models.ForeignKey(User)
	comment_to_audio = models.ForeignKey(Audio)
	
class Point(models.Model):
	value = models.IntegerField(default = 0)
	point_maker = models.ForeignKey(User)
	point_to_audio = models.ForeignKey(Audio)
	def __str__(self):
		return self.value
	

	





