from django.db import models
from product.models import NutritionalValue,ComponentProduct, Category, AdditionalIngredient
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    nutritional = models.ForeignKey(NutritionalValue, on_delete=models.CASCADE)
    product_composition = models.ManyToManyField(ComponentProduct)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    additional_ingredients = models.ManyToManyField(AdditionalIngredient)


