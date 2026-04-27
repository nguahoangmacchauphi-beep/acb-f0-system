def make_decision(state):
    if not isinstance(state, dict):
        raise ValueError("Invalid state")

    message = state.get("message", "")
    params = state.get("params", {})
    strength = params.get("echo_strength", 1.0)

    decision = {
        "action": "echo",
        "payload": message,
        "confidence": 0.8 * strength,
        "reason": "adaptive L4 decision"
    }

    return decision