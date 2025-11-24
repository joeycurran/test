def aggregate_scores(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def aggregate_weighted(scores, weights):
    if len(scores) != len(weights):
        raise ValueError("Length mismatch")
    total = sum(weights)
    if total == 0:
        raise ValueError("Zero weights")
    return sum(s * w for s, w in zip(scores, weights)) / total
