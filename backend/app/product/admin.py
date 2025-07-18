from django.contrib import admin
from product.models import Product, ProductImage, Category, ComponentProduct, NutritionalValue



class AdminProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('image',)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    inlines = [AdminProductImageInline]
    filter_horizontal = ('product_composition',)
    fields = ('name', 'price', 'nutritional','category','product_composition', 'description')


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass

@admin.register(ComponentProduct)
class AdminComponentProduct(admin.ModelAdmin):
    pass

@admin.register(NutritionalValue)
class AdminNutritionalValue(admin.ModelAdmin):
    pass