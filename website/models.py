from django.db import models

# Create your models here.
class Working(models.Model):

    title = models.CharField(max_length=100)
    descreption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')

class Servicing(models.Model):

    title = models.CharField(max_length=100)
    descreption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')

class Contacting(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

class Workings(models.Model):

    title = models.CharField(max_length=100)
    descreption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    link = models.CharField(max_length=1000)