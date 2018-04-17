from django.db import models

class Job(models.Model): #creates a new class in python, then saves it to the DB
    image = models.ImageField(upload_to='images/') #see documentation: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ImageField
    summary = models.CharField(max_length=1000) #CharField has a parameter: max_length
    link = models.URLField(max_length=200) #to make a link to the proper location
