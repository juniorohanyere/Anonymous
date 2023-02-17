from django.db import models
from django.db.models import Model
# Create your models here.

class Post (models.Model):

	icon = models.ImageField (blank = True)
	season_episode = models.CharField (max_length = 15, help_text = ('S00E00'), verbose_name = ("Season/Episode"))
	title = models.CharField (max_length = 100)
	description = models.CharField (max_length = 500, blank = True)
	date_added = models.DateField (verbose_name = ("Date Added"), auto_now_add = True)
	time = models.TimeField (verbose_name = ("Time"), auto_now_add = True)
	def __str__ (self):

		return "%s%s%s" % (self.season_episode," ", self.title)
