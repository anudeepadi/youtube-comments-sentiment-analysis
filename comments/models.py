from django.db import models

class Comment(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)
