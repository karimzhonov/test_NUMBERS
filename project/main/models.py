from django.db import models


class Product(models.Model):
    order_id = models.IntegerField('Заказ №', blank=True)
    price_dollor = models.FloatField('Стоимость, $', blank=True)
    price_rubl = models.FloatField('Стоимость, рубль', blank=True)
    delivery_date = models.DateField('Срок поставки', blank=True)

    def __str__(self):
        return f'{self.order_id}'