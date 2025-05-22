from django.db import models
from django.contrib.auth.models import User
import random
User._meta.get_field('email')._unique = True



class programme(models.Model):
	programme_name = models.CharField(max_length=150,unique=True)



	def __str__(self):
		return self.programme_name

class profile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	image =  models.ImageField(default='default.jpg' ,upload_to = 'profile_pics')


	def __str__(self):
		return self.user.username

