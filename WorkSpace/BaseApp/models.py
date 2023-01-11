from django.db import models

# Create your models here.

class Person (models.Model):

	First_Name = models.CharField (max_length = 50)
	Last_Name = models.CharField (max_length = 50)
	User_Name = models.CharField (max_length = 50)
	User_Email = models.CharField (max_length = 50)
	Age = models.IntegerField ()
