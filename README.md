# OKX Token Seller (SAHARA Auto Sell Bot)

Цей скрипт дозволяє автоматично виставити **лімітний ордер на продаж токенів SAHARA** через торговий API OKX.

## 🔧 Можливості

- Швидке створення ордера на продаж токенів SAHARA
- Лімітом за фіксованою ціною, яку ти задаєш
- Конфігурація через `.env` для безпеки

## ⚙️ Вимоги

- Python 3.7+
- API ключі OKX (API Key, Secret, Passphrase)
- Бібліотеки:
  - `requests`
  - `python-dotenv`

Встанови залежності:

```bash
    pip install -r requirements.txt
```

## ⚙️ .env файл
```dotenv
# OKX API Keys
OKX_API_KEY=your_api_key
OKX_API_SECRET=your_api_secret
OKX_PASSPHRASE=your_passphrase

# Token Sell Config
TOKEN_SYMBOL=SAHARA-USDT
SELL_AMOUNT=100
SELL_PRICE=0.15
```
> ⚠️ Ніколи не діліться вмістом .env файлу! Це дасть ПОВНИЙ доступ до вашого торгового акаунта OKX.