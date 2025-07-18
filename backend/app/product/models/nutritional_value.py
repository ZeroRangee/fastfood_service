from django.db import models




class NutritionalValue(models.Model):
    сarbohydrate = models.SmallIntegerField(blank=True,default=0)
    protein = models.SmallIntegerField(blank=True,default=0)
    fat = models.SmallIntegerField(blank=True, default=0)
    kcal = models.SmallIntegerField(blank=True, default=0 )
    
    
    def __str__(self):
        return f"Белки:{self.protein}, \n Жиры:{self.fat}, \n Углеводы:{self.сarbohydrate}, \n Ккал: {self.fat}"
    
    class Meta:
        verbose_name = "Пещевая ценность"
        verbose_name_plural = "Пещевая ценность продуктов"