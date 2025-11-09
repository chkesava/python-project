def is_valid_amount(value):
    try:
        amount = float(value)
        return amount > 0
    except ValueError:
        return False