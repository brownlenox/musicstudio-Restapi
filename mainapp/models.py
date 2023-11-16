from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    

#Many to Many
class Album(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    artists = models.ManyToManyField(Artist)
    artists = models.ManyToManyField(Artist, related_name="albums")

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title

# TODO add one to one