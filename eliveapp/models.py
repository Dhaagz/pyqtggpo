from django.db import models

class Channel(models.Model):
    title = models.CharField(max_length=32)
    topic = models.CharField(max_length=128)
    key = models.CharField(max_length=128, default="unset_key")
