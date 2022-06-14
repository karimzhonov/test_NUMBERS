import os
import requests
from datetime import date
from project.logger import logger
from main.models import Order


def send_message(product: Order):
    token = os.environ.get('TOKEN_BOT')
    # Request to Telegram api
    response = requests.post(
        url=f'https://api.telegram.org/bot{token}/sendMessage',
        data={'chat_id': 654147050, 'text': f'Срок поставки продукта (номер заказа-{product.order_id}) истек'}
    )
    # Logging errors
    if response.status_code != 200:
        response = response.json()
        logger.error(response)


def send_message_about_expiration_date():
    """Send message about expiration date of order"""
    logger.info('Start checking products delivery date')
    # Get all orders which not alerted about expiration date
    for product in Order.objects.filter(is_alerted_about_delivery_date=False):
        if product.delivery_date < date.today():
            send_message(product)
            product.is_alerted_about_delivery_date = True
            product.save()
