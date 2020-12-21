from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(max_length=200)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Brend(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    logo = models.ImageField(max_length=200)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def slug(self):
        return slugify(self.name)
    def __str__(self):
        return self.name
class Model(models.Model):
    name = models.CharField(max_length=200)
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    product_code = models.IntegerField(default=1)
    product_info = models.TextField(max_length=400)
    product_warranty = models.TextField(max_length=200)
    view_count = models.IntegerField(default=0, null=False, blank=True,editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    brend = models.ForeignKey(Brend, on_delete=models.SET_NULL, null=True,)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True,)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produktlar"
















# class ProductVariant(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     sale_percent = models.DecimalField(max_digits=2, decimal_places=2)
#     view_cnt = models.IntegerField(default=0, null=False, blank=True, editable=False)
#     created_at = models.DateTimeField(auto_now=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
#
#     def __str__(self):
#         return self.product
#     class Meta:
#         verbose_name = "Produktlist"
#         verbose_name_plural = "Produktlistlar"



