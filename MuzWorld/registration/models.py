from django.db import models

class User(models.Model):
	user_login = models.CharField(max_length = 50)
	user_name = models.CharField(max_length = 50)
	user_email = models.CharField(max_length = 100)
	user_password = models.IntegerField()
	def __str__(self):
		return self.user_name