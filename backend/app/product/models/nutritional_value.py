from django.db import models




class NutritionalValue(models.Model):
    name = models.CharField(max_length=255)