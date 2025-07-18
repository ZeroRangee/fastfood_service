
from rest_framework import serializers
from product.models import ProductImage

class ProductImage(serializers.ModelSerializer):
    
    
    class Meta:
        model = ProductImage
        fields = '__all__'