from rest_framework.generics import RetrieveAPIView, ListAPIView
from product.serializers import SerializerProductDetail, SerializerProductList
from product.models import Product




class ApiProductShowList(ListAPIView):
    serializer_class = SerializerProductList
    queryset = Product.objects.all()


class ApiProductShowDetail(RetrieveAPIView):
    serializer_class = SerializerProductDetail
