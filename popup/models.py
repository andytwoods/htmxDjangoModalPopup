from django.db import models


class EightiesKidsTVShows(models.Model):
    name = models.CharField(max_length=64)
    decade = models.IntegerField(default=1980)
    blurb = models.TextField()
    url = models.URLField()
    image_url = models.URLField()
