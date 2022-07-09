from django.urls import path, include
# from .views import SlidersList, ProductViewSet, UserViewSet, get_most_visit, get_latest_product
from rest_framework import routers
from .views import product_datail, get_products, most_visited, latest_product, get_sliders

app_name = "api"

router = routers.SimpleRouter()
# router.register('products', ProductViewSet, basename='products')
# router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('sliders', get_sliders, name='sliders'),
    path('most-visited', most_visited, name='m-v'),
    path('latest-products', latest_product, name='m-v'),
    path('products', get_products, name='all'),
    # path('products_category', get_category, name='all'),
    path('product-detail/<int:pk>', product_datail),

    # path('products/latest-products/', get_latest_product, name='latest'),
    # path('products/most-visited-products/', get_latest_product, name='most-visit'),

    ]


