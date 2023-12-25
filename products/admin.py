from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import Category, Product, Brand,WarrantyProduct, Seller
# Register your models here.


class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug',)

admin.site.register(Category,CategoryAdmin)

class BrandAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('brand_name',)}
    list_display = ('brand_name', 'slug',)

admin.site.register(Brand,BrandAdmin)

class WarrantyAdmin(ModelAdmin):
    prepopulated_fields = {'slug' : ('warranty_type',)}
    list_display = ('warranty_type', 'slug')
admin.site.register(WarrantyProduct, WarrantyAdmin)

class SellerAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('seller_name',)}
    list_display = ('seller_name', 'slug',)

admin.site.register(Seller,SellerAdmin)

class ProductAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price','brand','category','seller',)

admin.site.register(Product, ProductAdmin)