import requests
import pandas as pd
import os
from datetime import datetime

SYMBOLS = {
    "BTC": "BTCUSDT",
    "ETH": "ETHUSDT",
    "BNB": "BNBUSDT",
    "XRP": "XRPUSDT",
    "ADA": "ADAUSDT",
    "SOL": "SOLUSDT",
    "DOGE": "DOGEUSDT",
    "DOT": "DOTUSDT",
    "LTC": "LTCUSDT",
    "TRX": "TRXUSDT"
}

RAW_PATH = "../data/raw/raw_data.csv"
PROCESSED_PATH = "../data/processed/processed_data.csv"

def fetch_crypto_data(days=365):
    all_records = []

    for coin, symbol in SYMBOLS.items():
        print(f"Fetching {coin} historical OHLCV data...")

        url = "https://api.binance.com/api/v3/klines"
        params = {
            "symbol": symbol,
            "interval": "1d",
            "limit": days
        }

        response = requests.get(url, params=params)
        data = response.json()

        if isinstance(data, dict):
            print(f"Failed for {coin}")
            continue

        for row in data:
            all_records.append({
                "date": datetime.fromtimestamp(row[0] / 1000),
                "coin": coin,
                "open": float(row[1]),
                "high": float(row[2]),
                "low": float(row[3]),
                "close": float(row[4]),
                "volume": float(row[5])
            })

    if not all_records:
        print("No data collected")
        return

    df_raw = pd.DataFrame(all_records)
    df_processed = df_raw.copy()

    # Cleaning
    df_processed.dropna(inplace=True)
    df_processed.sort_values(["coin", "date"], inplace=True)

    os.makedirs("../data/raw", exist_ok=True)
    os.makedirs("../data/processed", exist_ok=True)

    df_raw.to_csv(RAW_PATH, index=False)
    df_processed.to_csv(PROCESSED_PATH, index=False)

    print("OHLCV historical data saved")
    print(f"Raw rows: {len(df_raw)}")
    print(f"Processed rows: {len(df_processed)}")

if __name__ == "__main__":
    fetch_crypto_data()
