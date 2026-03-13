import os
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_binance_client():
    api_key = os.getenv('BINANCE_API_KEY', '').strip()
    api_secret = os.getenv('BINANCE_SECRET_KEY', '').strip()

    if not api_key or not api_secret:
        raise ValueError("BINANCE_API_KEY and BINANCE_SECRET_KEY must be set in the .env file.")

    # Initialize client for Futures Testnet
    client = Client(api_key, api_secret, testnet=True)

    return client
