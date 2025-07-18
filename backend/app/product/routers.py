
from django.urls import path
from product.api import ApiProductShowList,ApiProductShowDetail

urlpatterns = [
    path('products', ApiProductShowList.as_view()),
    path('product', ApiProductShowDetail.as_view())
]