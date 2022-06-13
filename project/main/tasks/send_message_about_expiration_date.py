import os
import requests
from datetime import date
from project.logger import logger
from ..models import Product


def send_message(product: Product):
    token = os.environ.get('TOKEN_BOT')

    response = requests.post(
        url=f'https://api.telegram.org/bot{token}/sendMessage',
        data={'chat_id': 654147050, 'text': f'Срок поставки продукта (номер заказа-{product.order_id}) истек'}
    )
    if response.status_code != 200:
        response = response.json()
        logger.error(response)


def send_message_about_expiration_date():
    logger.info('Start checking products delivery date')
    for product in Product.objects.filter(is_alerted_about_delivery_date=False):
        if product.delivery_date < date.today():
            send_message(product)
            product.is_alerted_about_delivery_date = True
            product.save()
