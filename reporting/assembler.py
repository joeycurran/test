from analytics.engine import compute_profile

def build_report(values, a, b, c, w1, w2, w3):
    profile = compute_profile(values, a, b, c, w1, w2, w3)
    return {
        "metrics": profile,
        "summary": {
            "score": profile["alignment_weighted"] - profile["stability"],
            "flag": profile["consistency"] < 0.1
        }
    }
