import logging
from binance.exceptions import BinanceAPIException

logger = logging.getLogger('TradingBot.orders')

def place_futures_order(client, symbol, side, order_type, quantity, price=None):
    params = {
        'symbol': symbol.upper(),
        'side': side.upper(),
        'type': order_type.upper(),
        'quantity': quantity
    }

    if order_type.upper() == 'LIMIT':
        params['price'] = price
        params['timeInForce'] = 'GTC'  # Good Till Cancelled is standard for LIMIT orders

    logger.info(f"Sending order request: {params}")

    try:
        # Using futures_create_order for USDT-M Futures
        response = client.futures_create_order(**params)
        logger.info(f"Order placed successfully: {response}")
        return True, response
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.status_code} - {e.message}")
        return False, str(e)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return False, str(e)

def print_order_summary(success, data):

    print("-" * 40)
    if success:
        print("Order Placed")
        print(f"Order ID:      {data.get('orderId')}")
        print(f"Status:        {data.get('status')}")
        print(f"Symbol:        {data.get('symbol')}")
        print(f"Side:          {data.get('side')}")
        print(f"Executed Qty:  {data.get('executedQty')}")
        print(f"Avg Price:     {data.get('avgPrice', 'N/A')}")
    else:
        print("Order Failed")
        print(f"Error: {data}")
    print("-" * 40)
