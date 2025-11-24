def safe_div(a, b):
    if b == 0:
        return None
    return a / b

def safe_mean(values):
    if not values:
        return None
    return sum(values) / len(values)
