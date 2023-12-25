from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name='product'),
    path('category/<slug:category_slug>/', views.store, name='productbycat'),
    path('brand/<slug:brand_slug>/', views.store, name='productbybrand'),
    path('warranty/<slug:warranty_slug>/', views.store, name='productbywarranty'),
    path('seller/<slug:seller_slug>/', views.store, name='productbyseller'),
]
