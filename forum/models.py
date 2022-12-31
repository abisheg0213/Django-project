from django.db import models
from datetime import datetime
# Create your models here.
class project(models.Model):
    projname=models.CharField(max_length=250)
    date_of_start=models.DateTimeField(auto_now_add=True)
    proj_img=models.ImageField(null=True,blank=True,default='logo_social.png')
    tags=models.ManyToManyField('tag',blank=True)
    domain=models.CharField(max_length=100)
    desc=models.TextField(max_length=700,default="hello world")
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