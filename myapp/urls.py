from django.urls import path
from .views import ProductList, product_list, parse_view, analytics_view

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('parse/', parse_view, name='parse-wildberries'),
    path('api/products/', ProductList.as_view(), name='api-product-list'),
    path('analytics/', analytics_view, name='analytics'),
]


