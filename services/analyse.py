from core.metrics import MetricsEngine, legacy_compute_score
from core.helpers import safe_normalise

def analyse(values):
    engine = MetricsEngine()
    new_score = engine.compute_score(values)
    legacy_score = legacy_compute_score(values)
    normalised = safe_normalise(values)
    return {
        "new_score": new_score,
        "legacy_score": legacy_score,
        "normalised": normalised,
        "delta": new_score - legacy_score
    }
