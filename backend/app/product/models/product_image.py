from django.db import models
from product.models import Product


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_imgae/", verbose_name='Изображение')
    
    
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"