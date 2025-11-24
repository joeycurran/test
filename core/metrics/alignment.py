def triple_mean(a, b, c):
    return (a + b + c) / 3

def weighted_alignment(a, b, c, w1, w2, w3):
    total = w1 + w2 + w3
    return (a*w1 + b*w2 + c*w3) / total
