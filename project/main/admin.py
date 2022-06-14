from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'price_dollor', 'price_rubl', 'delivery_date', 'is_alerted_about_delivery_date']
    list_display_links = ('order_id',)
    search_fields = ('order_id', 'price_dollor', 'price_rubl')

    class Meta:
        model = Order
        fields = '__all__'