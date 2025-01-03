from django.db import models

class Kund(models.Model):
    namn = models.CharField(max_length=64)
