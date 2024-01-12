from django.db import models

# Create your models here.

  
class NewSong(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    file = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.title