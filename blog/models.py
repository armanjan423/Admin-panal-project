from django.db import models
import datetime

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.CharField(max_length=500, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-pub_date']

class AdminUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255) # Hashed
    is_staff = models.BooleanField(default=True)
