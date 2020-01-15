from django.db import models
from django.conf import settings


class Headline(models.Model):
    title=models.CharField(max_length=300)
    image=models.URLField()
    url=models.TextField()



    def __str__(self):
        return self.title

# Create your models here.
