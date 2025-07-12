from django.db import models
from nutritional_value import NutritionalValue
from component_product import ComponentProduct

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    nutritional = models.ForeignKey(NutritionalValue, on_delete=models.CASCADE)
    product_composition = models.ManyToManyField(ComponentProduct)