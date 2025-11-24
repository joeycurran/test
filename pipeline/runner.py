from services.analyse import analyse

def run_pipeline(values):
    result = analyse(values)
    if result["delta"] > 0:
        return "positive-shift", result
    return "negative-shift", result
