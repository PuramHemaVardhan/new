from django.db import models

# Create your models here.

class Topic(models.Model):
    Topicname=models.CharField(max_length=100)
    
class Webpages(models.Model):
    Topicname=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    URL=models.URLField()
    
class AcessRecord(models.Model):
    Name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    Date=models.DateField()
    Author=models.CharField(max_length=100)