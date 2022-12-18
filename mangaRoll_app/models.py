from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Manga Model
class Manga(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    this_image = models.ImageField(upload_to="mangaroll-image")

    def __str__(self):
        return str(self.name) + ' ' + str(self.id)

class Manger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    name=models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to="mangaroll-image")
    favorite_genre=models.CharField(max_length=200)
    objects = UserManager()

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.message)