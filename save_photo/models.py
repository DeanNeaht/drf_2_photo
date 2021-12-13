from django.db import models


class Image(models.Model):
    image1 = models.ImageField()
    image2 = models.ImageField()
