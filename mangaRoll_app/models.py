from django.db import models
from django.contrib.auth.models import User

# Manga Model
class Manga(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pdf = models.FileField(upload_to='mangaRoll_app/media/pdfs')
    image = models.FileField(upload_to='mangaRoll_app/media/images')

    def __str__(self):
        return str(self.name) + ' ' + str(self.id)

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.message)