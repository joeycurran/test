from pipeline.metrics_core import compute_consistency, compute_alignment

def derive_all(a, b, c):
    consistency = compute_consistency(a, b)
    alignment = compute_alignment(a, b, c)
    return {
        "consistency": consistency,
        "alignment": alignment,
        "combined": consistency * alignment,
    }
