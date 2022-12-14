from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime, timedelta

# Manga Model
class Manga(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    manga_id = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pdf = models.FileField(upload_to='mangaRoll_app/media/pdfs')
    image = models.FileField(upload_to='mangaRoll_app/media/images')

    def __str__(self):
        return str(self.name) + " ["+str(self.manga_id)+']'

# User Model
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return str(self.user) + " ["+str(self.name)+']' + " ["+str(self.email)+']'

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.message)