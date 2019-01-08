from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    post_title = models.CharField(max_length=70,default="Old Title")
    
    def __str__(self):
        return self.post_title