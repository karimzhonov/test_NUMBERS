from datetime import datetime
from project.logger import logger
from ..models import Product
from ..requests.cbr import dollor2rubl
from ..requests.sheet import get_sheet


def update_database():
    logger.info('Starting update database')
    products_db = list(Product.objects.all())
    for product in get_sheet():
        if _validate_sheet_data(product):
            product['price_rubl'] = dollor2rubl(product['price_dollor'])
            products_db_filtered = list(filter(lambda p: p.pk == int(product['id']), products_db))
            if len(products_db_filtered):
                product_db = products_db_filtered[0]
                _update(product_db, product)
            else:
                product_db = Product.objects.create(**product)
                logger.debug(f'Product {product_db.order_id} created')


def _update(product_db: Product, product: dict):
    save = False
    if product_db.order_id != int(product.get('order_id', None)):
        save = True
        product_db.order_id = product['order_id']
    if product_db.price_dollor != float(product.get('price_dollor', None)):
        save = True
        product_db.price_dollor = product['price_dollor']
    if product_db.price_rubl != float(product.get('price_rubl', None)):
        save = True
        product_db.price_rubl = product['price_rubl']
    if str(product_db.delivery_date) != product.get('delivery_date', None):
        save = True
        product_db.delivery_date = product['delivery_date']

    if save:
        product_db.save()
        logger.debug(f'Product {product_db.order_id} updated')


def _validate_sheet_data(data: dict):
    data['delivery_date'] = _validate_date(data.get('delivery_date', None))
    if data['delivery_date'] is None: return False
    return _validate_numbers(data['id']) \
           and _validate_numbers(data['order_id']) \
           and _validate_numbers(data['price_dollor'])


def _validate_numbers(obj):
    try:
        float(obj)
        return True
    except ValueError:
        return False


def _validate_date(obj):
    if obj is None: return
    _format = '%d.%m.%Y'
    try:
        obj = obj.replace('-', '.')
        if len(obj) == 8:
            # 01.01.20
            _format = '%d.%m.%y'
        return str(datetime.strptime(obj, _format).date())
    except ValueError or TypeError:
        pass
