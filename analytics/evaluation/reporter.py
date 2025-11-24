from analytics.transforms.combiner import combine_all

def build_final_report(scores, weights, label="default"):
    base = combine_all(scores, weights)
    base["label"] = label
    return base
