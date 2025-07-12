from django.db import models



class ComponentProduct(models.Model):
    name = models.CharField(max_length=255)