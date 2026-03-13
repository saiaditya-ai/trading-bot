import argparse
import sys
from bot.logging_config import setup_logging
from bot.validators import validate_args
from bot.client import get_binance_client
from bot.orders import place_futures_order, print_order_summary

def main():
    logger = setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot CLI")
    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side (BUY or SELL)")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type (MARKET or LIMIT)")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    # 1. Validate inputs
    is_valid, errors = validate_args(args)
    if not is_valid:
        for error in errors:
            logger.error(f"Validation Error: {error}")
            print(f"Error: {error}")
        sys.exit(1)

    logger.info(f"Starting order process for {args.symbol} {args.side} {args.type}")

    # 2. Get Binance Client
    try:
        client = get_binance_client()
    except Exception as e:
        logger.error(f"Initialization Error: {str(e)}")
        print(f"Error: Could not initialize Binance client. {str(e)}")
        sys.exit(1)

    # 3. Place order
    success, result = place_futures_order(
        client=client,
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    # 4. Show results
    print_order_summary(success, result)

if __name__ == "__main__":
    main()
