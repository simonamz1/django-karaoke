from django.db import models

# Write your models here
class Performer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    length = models.IntegerField(default=0)

    def __str__(self):
        return "{} by {}".format(self.title, self.artist)
