def grade_classification(pred):
    if pred == "billing_issue":
        return 1.0
    return 0.0


def grade_priority(pred):
    if pred == "high":
        return 1.0
    return 0.0


def grade_response(response):
    response = response.lower()

    if "refund" in response:
        return 1.0
    elif "sorry" in response:
        return 0.5
    return 0.0
