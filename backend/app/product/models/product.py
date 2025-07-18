from django.db import models
from product.models import NutritionalValue,ComponentProduct, Category, AdditionalIngredient

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    nutritional = models.ForeignKey(NutritionalValue, on_delete=models.CASCADE, verbose_name="КБЖУ")
    product_composition = models.ManyToManyField(ComponentProduct, verbose_name="Ингредиенты")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    additional_ingredients = models.ManyToManyField(AdditionalIngredient, verbose_name="Состав")
    
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


