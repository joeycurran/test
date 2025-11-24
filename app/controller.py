from services.analytics_service import aggregate_scores

def handle_request(scores, weights):
    return aggregate_scores(scores, weights)
