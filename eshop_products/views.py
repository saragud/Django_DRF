from django.views.generic import ListView
from .models import Product, ProductGallery


class ProductList(ListView):
    def get_queryset(self):
        return Product.objects.filter(active=True)