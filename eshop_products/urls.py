from django.urls import path, include
from .views import ProductList


app_name = "eshop_products"


urlpatterns = [
    path('', ProductList.as_view(), name='plist'),
    ]
