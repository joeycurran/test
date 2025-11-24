from analytics.core.aggregation import aggregate_scores, aggregate_weighted
from analytics.core.normalisation import min_max_normalise

def combine_all(scores, weights):
    raw = aggregate_scores(scores)
    weighted = aggregate_weighted(scores, weights)
    norm = min_max_normalise(scores)
    return {
        "raw": raw,
        "weighted": weighted,
        "normalised": norm,
        "variance": max(scores) - min(scores) if scores else 0
    }
