def validate_input(input_data):
    if input_data is None:
        raise ValueError("Input cannot be None")

    if not isinstance(input_data, dict):
        raise ValueError("Input must be a dictionary")

    if "message" not in input_data:
        raise ValueError("Missing key: message")

    return input_data