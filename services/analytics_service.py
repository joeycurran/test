from utils.math_ops import compute_moving_avg, compute_weighted_avg

def aggregate_scores(scores, weights):
    avg = compute_moving_avg(scores)
    weighted = compute_weighted_avg(scores, weights)
    return {"average": avg, "weighted": weighted}
