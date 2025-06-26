# Standard Libraries
import os
import time
import base64
import hmac
import hashlib
import json

# Third-party Libraries
import requests
from dotenv import load_dotenv


# === Завантаження змінних з .env ===
load_dotenv()

API_KEY = os.getenv('OKX_API_KEY')
API_SECRET = os.getenv('OKX_API_SECRET')
PASSPHRASE = os.getenv('OKX_PASSPHRASE')

TOKEN_SYMBOL = os.getenv('TOKEN_SYMBOL', 'SAHARA-USDT')
SELL_AMOUNT = os.getenv('SELL_AMOUNT', '100')
SELL_PRICE = os.getenv('SELL_PRICE', '0.15')

OKX_URL = 'https://www.okx.com'
ENDPOINT = '/api/v5/trade/order'
METHOD = 'POST'
CONTENT_TYPE = 'application/json'


def get_iso_timestamp():
    return time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())


def generate_signature(timestamp, method, request_path, body, secret_key):
    message = timestamp + method.upper() + request_path + body
    mac = hmac.new(bytes(secret_key, encoding='utf-8'), bytes(message, encoding='utf-8'), digestmod=hashlib.sha256)
    return base64.b64encode(mac.digest()).decode()


def place_limit_order():
    timestamp = get_iso_timestamp()

    body = json.dumps({
        "instId": TOKEN_SYMBOL,
        "tdMode": "cash",
        "side": "sell",
        "ordType": "limit",
        "px": SELL_PRICE,
        "sz": SELL_AMOUNT
    })

    sign = generate_signature(timestamp, METHOD, ENDPOINT, body, API_SECRET)

    headers = {
        'Content-Type': CONTENT_TYPE,
        'OK-ACCESS-KEY': API_KEY,
        'OK-ACCESS-SIGN': sign,
        'OK-ACCESS-TIMESTAMP': timestamp,
        'OK-ACCESS-PASSPHRASE': PASSPHRASE
    }

    response = requests.post(OKX_URL + ENDPOINT, headers=headers, data=body)

    print(f"[{response.status_code}] {response.text}")


def spam_limit_order(max_attempts=50, delay_sec=0.3):
    """
    Надсилає ордер багаторазово, поки не отримає успіх або не досягне ліміту спроб.
    :param max_attempts: максимальна кількість спроб
    :param delay_sec: затримка між спробами в секундах
    """
    for attempt in range(1, max_attempts + 1):
        print(f"[{attempt}] Відправляю ордер на продаж {SELL_AMOUNT} {TOKEN_SYMBOL} по {SELL_PRICE} USDT...")

        timestamp = get_iso_timestamp()

        body = json.dumps({
            "instId": TOKEN_SYMBOL,
            "tdMode": "cash",
            "side": "sell",
            "ordType": "limit",
            "px": SELL_PRICE,
            "sz": SELL_AMOUNT
        })

        sign = generate_signature(timestamp, METHOD, ENDPOINT, body, API_SECRET)

        headers = {
            'Content-Type': CONTENT_TYPE,
            'OK-ACCESS-KEY': API_KEY,
            'OK-ACCESS-SIGN': sign,
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': PASSPHRASE
        }

        try:
            response = requests.post(OKX_URL + ENDPOINT, headers=headers, data=body)
            data = response.json()

            if response.status_code == 200 and data.get("code") == '0':
                print("✅ Ордер успішно створено:", data.get("data"))
                break
            else:
                print(f"⚠️ Помилка: {data.get('msg', response.text)}")

        except Exception as e:
            print(f"❌ Виняток при відправці: {e}")

        time.sleep(delay_sec)
    else:
        print("⛔ Досягнуто ліміту спроб, ордер не був прийнятий.")


if __name__ == '__main__':
    # place_limit_order()
    spam_limit_order(max_attempts=100, delay_sec=0.1)
