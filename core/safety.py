def safe_execute(func, *args, **kwargs):
    try:
        return {
            "ok": True,
            "result": func(*args, **kwargs)
        }
    except Exception as e:
        return {
            "ok": False,
            "error": str(e)
        }


def safe_state(state):
    if state is None:
        return {"status": "RECOVERED", "version": 0}

    if not isinstance(state, dict):
        return {"status": "FIXED_TYPE", "version": 0}

    return state