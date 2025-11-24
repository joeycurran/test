from utils.math_ops import compute_moving_avg, compute_weighted_avg
from utils.safe_ops import safe_div

def aggregate_scores(scores, weights):
    avg = compute_moving_avg(scores)
    weighted = compute_weighted_avg(scores, weights)
    stability = safe_div(weighted, avg)
    return {"average": avg, "weighted": weighted, "stability": stability}
