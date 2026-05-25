def validate_record(quantity, unit):

    errors = []

    suspicious = False

    if quantity <= 0:
        errors.append("Quantity must be positive")

    valid_units = [
        'liters',
        'kwh',
        'km',
        'miles'
    ]

    if unit.lower() not in valid_units:
        errors.append("Invalid unit")

    if quantity > 10000:
        suspicious = True
        errors.append("Unusually high quantity detected")

    return {
        "suspicious": suspicious,
        "message": ", ".join(errors)
    }