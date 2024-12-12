from django.db import models

class Kunder(models.Model):
    namn = models.CharField(max_length=64)
