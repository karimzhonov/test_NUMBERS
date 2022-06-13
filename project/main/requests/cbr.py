"""Get rates from central bank Russian"""
import requests


def get_rates():
    response = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    return response['rates']


def dollor2rubl(price):
    rates = get_rates()
    price_rubl = float(price) / rates['USD']
    price_rubl = round(price_rubl * 100) / 100
    return price_rubl
