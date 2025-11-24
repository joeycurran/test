def ratio(a, b):
    if b == 0:
        raise ZeroDivisionError("b cannot be zero")
    return a / b

def stability(values):
    if not values:
        return 0
    mean = sum(values) / len(values)
    return sum(abs(v - mean) for v in values)
