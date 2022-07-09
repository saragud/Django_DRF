from django.contrib import admin

# Register your models here.
from .models import OrderDetail, Order

admin.site.register(Order)
admin.site.register(OrderDetail)