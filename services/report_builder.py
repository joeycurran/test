from utils.math_ops import (
    compute_weighted_avg,
    compute_bias_adjusted_avg,
    normalise_vector,
)

def build_report(scores, weights, bias):
    weighted = compute_weighted_avg(scores, weights)
    adjusted = compute_bias_adjusted_avg(scores, bias)
    normalised = normalise_vector(scores)
    return {
        "weighted": weighted,
        "adjusted": adjusted,
        "normalised": normalised,
        "delta": adjusted - weighted,
    }
