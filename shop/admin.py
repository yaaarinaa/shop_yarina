from django.contrib import admin
from .models import Product, Manufacturer

admin.site.register(Manufacturer)
admin.site.register(Product)