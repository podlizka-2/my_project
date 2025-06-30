from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    reviews_count = models.PositiveIntegerField(default=0)
    query = models.CharField(max_length=255, blank=True)  # Добавлено поле для запроса
    

    def __str__(self):
        return self.name
    
    def discount_percent(self):
        if self.price and self.sale_price and self.price > 0:
            return round((self.price - self.sale_price) / self.price * 100, 2)
        return 0
