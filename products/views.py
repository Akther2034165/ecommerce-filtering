from django.shortcuts import render
from .models import Product, Category, Seller, WarrantyProduct, Brand
from django.shortcuts import get_object_or_404
# Create your views here.

def store(request, category_slug=None, brand_slug=None, seller_slug=None, warranty_slug=None):
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')
    products = Product.objects.all()

    if min_price is not None and max_price is not None:
        try:
            products = products.filter(price__range=(min_price, max_price))
        except ValueError:
            pass

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    elif brand_slug is not None:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)

    elif seller_slug is not None:
        seller = get_object_or_404(Seller, slug=seller_slug)
        products = products.filter(seller=seller)

    elif warranty_slug is not None:
        warranty = get_object_or_404(WarrantyProduct, slug=warranty_slug)
        products = products.filter(warranty=warranty)

    categories = Category.objects.all()
    brands = Brand.objects.all()
    warranties = WarrantyProduct.objects.all()
    sellers = Seller.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'brands': brands,
        'warranties': warranties,
        'sellers': sellers,
        'min_price': min_price,
        'max_price': max_price,
    }

    return render(request, 'store.html', context)
