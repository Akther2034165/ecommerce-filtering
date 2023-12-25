from django.db import models


    
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True) 
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20) 
       
    def __str__(self):
        return self.brand_name
    
class WarrantyProduct(models.Model):
    warranty_type = models.CharField(max_length = 50, null = True)
    slug = models.SlugField(max_length = 50)
    def __str__(self):
        return self.warranty_type
    
class Seller(models.Model):
    seller_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20) 
       
    def __str__(self):
        return self.seller_name
    
    
class Product(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    product_name = models.CharField(max_length=20, unique = True)
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/products')
    warranty = models.ForeignKey(WarrantyProduct, on_delete = models.CASCADE, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name