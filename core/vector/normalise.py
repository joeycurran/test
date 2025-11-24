def l1(values):
    total = sum(abs(v) for v in values)
    if total == 0:
        return [0 for _ in values]
    return [v / total for v in values]

def l2(values):
    total = sum(v*v for v in values) ** 0.5
    if total == 0:
        return [0 for _ in values]
    return [v / total for v in values]
