import requests
import json

#__all__= ['fetch_order_book']  # imports control

def fetch_order_book(symbol: str, limit: int = 5, filename: str = "order_book.json"):
    """Fetches order book from Binance API and saves to file."""
    url = "https://api.binance.com/api/v3/depth"
    params = {"symbol": symbol, "limit": limit}
    try:
        r = requests.get(url, params=params, timeout=5)
        r.raise_for_status()
        data = r.json()
        with open(filename, "w") as f:
            json.dump(data, f)
        print(f"Order book saved to /data/raw/{filename}")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


