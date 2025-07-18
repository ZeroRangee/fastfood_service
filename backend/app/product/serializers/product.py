from rest_framework import serializers
from product.models import Product
from product.serializers import ProductImage





class SerializerProductDetail(serializers.ModelSerializer):
    images = ProductImage(many=True, read_only=True)
    
    class Meta:
        model = Product
        
class SerializerProductList(serializers.ModelSerializer):
    images = ProductImage(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'images']