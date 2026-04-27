def create_state(valid_input):
    if not isinstance(valid_input, dict):
        raise ValueError("State must be created from dict input")

    state = {
        "message": valid_input.get("message"),
        "status": "INIT",
        "version": 1,

        # 🔥 adaptive params (STEP 4)
        "params": {
            "echo_strength": 1.0
        }
    }

    return state