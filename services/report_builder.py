from utils.math_ops import compute_weighted_avg, compute_bias_adjusted_avg

def build_report(scores, weights, bias):
    weighted = compute_weighted_avg(scores, weights)
    adjusted = compute_bias_adjusted_avg(scores, bias)
    return {
        "weighted": weighted,
        "adjusted": adjusted,
        "delta": adjusted - weighted,
    }
