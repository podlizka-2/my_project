import re
import requests
from .models import Product

def parse_wildberries(query):
    # Удаляем ВСЕ существующие товары перед парсингом новых
    print(f"Очищаем базу перед запросом: {query}")
    deleted_count, _ = Product.objects.all().delete()
    print(f"Удалено товаров: {deleted_count}")
    
    url = "https://search.wb.ru/exactmatch/ru/common/v4/search"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json'
    }
    params = {
        'query': query,
        'resultset': 'catalog',
        'sort': 'popular',
        'page': 1,
        'appType': 1,
        'dest': -1257786,
        'regions': 80,  # Россия
        'curr': 'rub',
        'lang': 'ru',
        'locale': 'ru',
        'spp': 0,
        'reg': 1,
        'prun': 1  # Только релевантные товары
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Проверяем наличие данных
        if not data.get('data') or not data['data'].get('products'):
            print("Нет данных в ответе API")
            return
        
        # Создаем regex-паттерн для поиска ключевых слов
        words = query.split()
        if words:
            # Исправление: правильное формирование regex-паттерна
            pattern_str = r'\b(' + '|'.join(re.escape(word) for word in words) + r')\b'
            query_pattern = re.compile(pattern_str, re.IGNORECASE)
        else:
            query_pattern = None
        
        # Базовый URL для товаров Wildberries
        base_url = "https://www.wildberries.ru/catalog/"
        
        # Счетчики для статистики
        total_products = 0
        saved_products = 0
        
        for product in data['data']['products']:
            total_products += 1
            name = product.get('name', '')
            # Если есть паттерн и название не соответствует - пропускаем
            if query_pattern and not query_pattern.search(name):
                continue
                
            price = product.get('priceU')
            if price is not None:
                price = price / 100
            else:
                continue  # Пропускаем товары без цены
                
            sale_price = product.get('salePriceU')
            if sale_price is not None:
                sale_price = sale_price / 100
            else:
                sale_price = price  # Если нет скидки, то sale_price = цена
                
            rating = product.get('reviewRating')
            if rating == 0:  # Если рейтинг 0, считаем его отсутствующим
                rating = None
                
            reviews_count = product.get('feedbacks', 0)
            
            # Формируем ссылку на товар
            product_id = product.get('id')
            product_url = f"{base_url}{product_id}/detail.aspx" if product_id else None
            
            # Создаем товар
            try:
                Product.objects.create(
                    id=product_id,
                    name=name,
                    price=price,
                    sale_price=sale_price,
                    rating=rating,
                    reviews_count=reviews_count,
                    query=query,
                    url=product_url  # Сохраняем ссылку
                )
                saved_products += 1
            except Exception as e:
                print(f"Ошибка при сохранении товара {product_id}: {str(e)}")
            
        print(f"Успешно сохранено товаров: {saved_products}/{total_products}")
            
    except Exception as e:
        print(f"Ошибка парсинга: {str(e)}")