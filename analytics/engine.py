from core.metrics.consistency import ratio, stability
from core.metrics.alignment import triple_mean, weighted_alignment
from core.vector.normalise import l1, l2

def compute_profile(values, a, b, c, w1, w2, w3):
    return {
        "consistency": ratio(a, b),
        "stability": stability(values),
        "alignment_plain": triple_mean(a, b, c),
        "alignment_weighted": weighted_alignment(a, b, c, w1, w2, w3),
        "l1_norm": l1(values),
        "l2_norm": l2(values),
    }
