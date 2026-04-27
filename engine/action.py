def execute_action(decision):
    if not isinstance(decision, dict):
        raise ValueError("Invalid decision")

    action = decision.get("action")

    if action == "echo":
        return {
            "status": "ok",
            "output": decision.get("payload")
        }

    return {
        "status": "unknown_action",
        "output": None
    }