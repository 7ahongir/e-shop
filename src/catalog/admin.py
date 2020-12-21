from django.contrib import admin


from .models import Category, Product, Brend, Model


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product_code']
class BrendAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug']
class MadelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Category, CatalogAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brend, BrendAdmin)
admin.site.register(Model, MadelAdmin)