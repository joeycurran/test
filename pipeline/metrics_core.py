def compute_consistency(metric_a, metric_b):
    if metric_b == 0:
        return 0
    return metric_a / metric_b

def compute_alignment(metric_a, metric_b, metric_c):
    return (metric_a + metric_b + metric_c) / 3
