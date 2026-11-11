from django.db import models
from django.utils import timezone
from datetime import timedelta

class Manufacturer(models.Model):
    name = models.CharField("Название производителя", max_length=100)
    def __str__(self): return self.name

class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Изображение", upload_to='products/', blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель")
    in_stock = models.BooleanField("В наличии", default=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self): return self.name