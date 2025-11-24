def min_max_normalise(values):
    if not values:
        return values
    mn = min(values)
    mx = max(values)
    if mx == mn:
        return [0 for _ in values]
    return [(v - mn) / (mx - mn) for v in values]
