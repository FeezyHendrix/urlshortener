from django.db import models
import string
import random

# Create your models here.
class Url(models.Model):
    real_url = models.CharField(max_length = 240)
    generated_link = models.CharField(max_length = 240)
    url_views = models.IntegerField(default=0)


    def __str__(self):
        return self.generated_link
