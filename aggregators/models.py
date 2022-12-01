from django.db import models

# Create your models here.


class Article(models.Model):

    name = models.CharField(max_length=100)
    created_time = models.DateTimeField()
    url = models.URLField()
    series_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)
    topic = models.CharField(max_length=50, default="General")

    def __str__(self):
        return f"{self.series_name}: {self.name}"

class Channel(models.Model):

    rss_feed = models.URLField()
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=50, default="General")

    def __str__(self):
        return f"{self.name}: {self.topic}"

