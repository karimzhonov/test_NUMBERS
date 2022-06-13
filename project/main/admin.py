from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'price_dollor', 'price_rubl', 'delivery_date', 'is_alerted_about_delivery_date']
    list_display_links = ('order_id',)
    search_fields = ('order_id', 'price_dollor', 'price_rubl')

    class Meta:
        model = Product
        fields = '__all__'