def validate_args(args):
    errors = []

    # 1. side validation
    if args.side.upper() not in ["BUY", "SELL"]:
        errors.append(f"Invalid side: {args.side}. Must be BUY or SELL.")

    # 2. type validation
    if args.type.upper() not in ["MARKET", "LIMIT"]:
        errors.append(f"Invalid order type: {args.type}. Must be MARKET or LIMIT.")

    # 3. quantity validation
    try:
        if float(args.quantity) <= 0:
            errors.append("Quantity must be a positive number.")
    except (ValueError, TypeError):
        errors.append("Quantity must be a valid number.")

    # 4. price validation for LIMIT orders
    if args.type.upper() == "LIMIT":
        if args.price is None:
            errors.append("Price is required for LIMIT orders.")
        else:
            try:
                if float(args.price) <= 0:
                    errors.append("Price must be a positive number for LIMIT orders.")
            except (ValueError, TypeError):
                errors.append("Price must be a valid number.")

    if errors:
        return False, errors
    return True, []
