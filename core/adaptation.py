def apply_adaptation(state, feedback):
    if not isinstance(state, dict):
        return state

    params = state.get("params", {})
    strength = params.get("echo_strength", 1.0)

    signal = feedback.get("signal")

    # 🔥 bounded update rule
    if signal == "POSITIVE":
        strength += 0.05
    elif signal == "NEGATIVE":
        strength -= 0.05

    # clamp (GIỚI HẠN AN TOÀN)
    strength = max(0.5, min(1.5, strength))

    state["params"]["echo_strength"] = strength

    return state