from django.shortcuts import render
from .models import Product


def index(request):
    context = {
        'keys': ['Id', 'Заказ №', "Стоимость (доллор)", 'Стоимость (рубль)', 'Срок поставки'],
        'products': Product.objects.all().order_by('pk')
    }
    return render(request, 'main/index.html', context, status=200)
