class MetricsEngine:
    def compute_score(self, values):
        if not values:
            raise ValueError("values cannot be empty")
        product = 1
        for v in values:
            product *= v
        return product ** (1 / len(values))

def legacy_compute_score(values):
    if not values:
        return 0
    return sum(values) / len(values)
