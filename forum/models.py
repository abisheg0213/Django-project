from django.db import models
from datetime import datetime
# Create your models here.
class project(models.Model):
    projname=models.CharField(max_length=250)
    date_of_start=models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField('tag',blank=True)
    domain=models.CharField(max_length=100)
    def __str__(self):
        return self.projname

class review(models.Model):
    project=models.ForeignKey(project,on_delete=models.CASCADE)
    comments=models.TextField()
    reviewer=models.CharField(max_length=250)
    def __str__(self):
        return self.reviewer
class tag(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name