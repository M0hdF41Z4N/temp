from email.policy import default
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField()
    timeStamp = models.DateTimeField('Date published',blank=True)
    slug = models.CharField(default="hello",max_length=130)
    # Need to attach attach
    # images
    # likes
    # comments

    def __str__(self):
        return "Posted by " + self.author
    