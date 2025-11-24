from utils.math_ops import compute_moving_avg

def old_run(values):
    avg = compute_moving_avg(values)
    return {"avg": avg}
