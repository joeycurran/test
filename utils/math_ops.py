def compute_moving_avg(values):
    if not values:
        return 0
    return sum(values) / len(values)

def compute_weighted_avg(values, weights):
    if len(values) != len(weights):
        raise ValueError("Length mismatch")
    total = sum(weights)
    if total == 0:
        raise ValueError("Zero total weight")
    return sum(v * w for v, w in zip(values, weights)) / total

def compute_bias_adjusted_avg(values, bias):
    return sum(values) / len(values) + bias
