import requests
import os


def get_currency_codes() -> list:
    """
    Функция получает и возвращает список кодов валют
    """
    res = requests.get(f'https://api.currencyapi.com/v3/currencies?apikey={os.getenv("API_CONVERTER")}&currencies=')
    return sorted(list(res.json()['data'].keys()))


def get_convert_sum(from_: str, to: str, sum_: int) -> int:
    """
    Функция конвертирует валюту from_ в валюту to,
    умножаем получаемое значение на sum_ и возвращает
    """
    res = requests.get(
        f'https://api.currencyapi.com/v3/latest?'
        f'apikey={os.getenv("API_CONVERTER")}&'
        f'currencies={to}&'
        f'base_currency={from_}'
    ).json()['data'][to]['value']
    return round(res * sum_, 2)
