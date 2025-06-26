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

## 🔩 Активувати venv
- Windows
```bash
    python -m venv venv
    venv\Scripts\activate
```

- macOS / Linux
```bash
    python3 -m venv venv
  source venv/bin/activate
```

## 🔩️ Встанови залежності
```bash
    pip install -r requirements.txt
```


## 🔩 .env файл
```dotenv
# OKX API Keys
OKX_API_KEY=your_api_key
OKX_API_SECRET=your_api_secret
OKX_PASSPHRASE=your_passphrase

# Token Sell Config
TOKEN_SYMBOL=SAHARA-USDT
SELL_AMOUNT=4000
SELL_PRICE=0.25

# Unix час у секундах (в локальному часі вашого пристроя!)
START_TIME_YEAR=2025
START_TIME_MONTH=6
START_TIME_DAY=26
START_TIME_HOUR=14
START_TIME_MINUTES=59
START_TIME_SECONDS=59
```
> ⚠️ Ніколи не діліться вмістом .env файлу! Це дасть ПОВНИЙ доступ до вашого торгового акаунта OKX.