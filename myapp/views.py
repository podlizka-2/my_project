from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from .task import parse_wildberries
from django.http import JsonResponse
import threading
import subprocess
from django.views.decorators.csrf import csrf_exempt
import sys


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price', 'sale_price', 'rating', 'reviews_count']

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

    
def list(self, request, *args, **kwargs):
    # Логирование SQL-запроса
    print("SQL Query:", self.get_queryset().query)
    return super().list(request, *args, **kwargs)


@csrf_exempt
def parse_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()
        if query:
            try:
                python_path = sys.executable
                
                def run_parser():
                    subprocess.run([
                        python_path, 'manage.py', 'parse_wildberries', 
                        query
                    ], check=True)
                
                thread = threading.Thread(target=run_parser)
                thread.daemon = True
                thread.start()
                
                return JsonResponse({
                    'status': 'success', 
                    'message': f'Парсинг для "{query}" запущен!'
                })
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        return JsonResponse({'status': 'error', 'message': 'Пустой запрос'})
    return render(request, 'parse.html')

def analytics_view(request):
    return render(request, 'index.html')