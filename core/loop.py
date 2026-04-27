from core.validator import validate_input
from core.state import create_state
from engine.decision import make_decision
from engine.action import execute_action
from engine.eval import evaluate
from storage.history import save_history
from core.adaptation import apply_adaptation
from storage.memory import append_memory, load_memory


def build_feedback(evaluation):
    score = evaluation.get("score", 0)

    if score >= 0.8:
        signal = "POSITIVE"
    elif score >= 0.5:
        signal = "NEUTRAL"
    else:
        signal = "NEGATIVE"

    return {
        "signal": signal,
        "score": score
    }


def run_loop(input_data):
    try:
        # 1. validate
        valid_input = validate_input(input_data)

        # 2. state
        state = create_state(valid_input)

        # 3. decision
        decision = make_decision(state)

        # 4. action
        result = execute_action(decision)

        # 5. evaluation
        evaluation = evaluate(result, decision, state)

        # 6. feedback
        feedback = build_feedback(evaluation)

        # 7. adaptation
        state = apply_adaptation(state, feedback)

        # 8. memory
        append_memory({
            "input": valid_input,
            "feedback": feedback,
            "state_params": state.get("params"),
            "score": evaluation.get("score")
        })

        # 9. history
        save_history({
            "input": valid_input,
            "state": state,
            "decision": decision,
            "result": result,
            "evaluation": evaluation,
            "feedback": feedback
        })

        return {
            "ok": True,
            "result": result,
            "evaluation": evaluation,
            "feedback": feedback
        }

    except Exception as e:
        return {
            "ok": False,
            "error": str(e)
        }