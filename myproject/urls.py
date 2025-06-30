"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import ProductList, analytics_view, parse_view, product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductList.as_view(), name='api-product-list'),  # Исправлено
    path('', analytics_view, name='home'),
    path('parse/', parse_view, name='parse'),
    path('products/', product_list, name='product-list'),
    path('analytics/', analytics_view, name='analytics'),
]
