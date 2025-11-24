def compute_adjusted_sum(values, adjust):
    return sum(values) + adjust

def compute_adjusted_product(values, adjust):
    p = 1
    for v in values:
        p *= v
    return p + adjust
