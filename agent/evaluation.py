EVALUATION_WEIGHTS = {
    "goal_understanding": 20,
    "risk_detection": 15,
    "priority_reasoning": 25,
    "architecture_quality": 20,
    "execution_planning": 15,
    "clarity": 5
}

def calculate_score(scores: dict) -> dict:
    weighted_score = 0

    for category, weight in EVALUATION_WEIGHTS.items():
        category_score = scores.get(category, 0)

        weighted_score += category_score * weight

    normalized_score = weighted_score * 10

    return {
        "raw_scores": scores,
        "final_score": normalized_score,
        "max_score": 10000
    }

def evaluate_analysis(analysis_results: dict) -> dict:
    scores = {
        "goal_understanding": 8,
        "risk_detection": 8,
        "priority_reasoning": 9,
        "architecture_quality": 8,
        "execution_planning": 8,
        "clarity": 9
    }

    return calculate_score(scores)

