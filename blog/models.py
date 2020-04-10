from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #one to many relationship

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #auto_now_add will not let you change the date, so we will import something
    author = models.ForeignKey(User, on_delete=models.CASCADE)
