def evaluate(result, decision=None, state=None):
    # L4 stub evaluator (chưa self-improve)
    score = 1.0 if result.get("status") == "ok" else 0.0

    return {
        "score": score,
        "valid": score == 1.0,
        "note": "L4 passive evaluation"
    }