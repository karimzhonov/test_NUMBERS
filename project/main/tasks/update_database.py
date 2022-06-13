from datetime import datetime
from ..models import Product
from ..requests.cbr import dollor2rubl


def update_database(data: list[dict, ...]):
    products_db = list(Product.objects.all())
    for product in data:
        product['delivery_date'] = str(datetime.strptime(product['delivery_date'], '%d.%m.%Y').date())
        product['price_rubl'] = dollor2rubl(product['price_dollor'])
        products_db_filtered = list(filter(lambda p: p.pk == int(product['id']), products_db))
        if len(products_db_filtered):
            product_db = products_db_filtered[0]
            product_db.order_id = product['order_id']
            product_db.price_dollor = product['price_dollor']
            product_db.price_rubl = product['price_rubl']
            product_db.delivery_date = product['delivery_date']
            product_db.save(force_update=True)
        else:
            Product.objects.create(**product)
    print('Updated')
    print('Updated')
    print('Updated')
