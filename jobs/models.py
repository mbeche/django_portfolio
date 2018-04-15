from django.db import models

class Job(models.Model): #creates a new class in python, then saves it to the DB
    image = models.ImageField(upload_to='images/') #see documentation: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ImageField
    summary = models.CharField(max_length=200) #CharField has a parameter: max_length
