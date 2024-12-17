def validate_input(value, expected_type):
    try:
        return expected_type(value)
    except ValueError:
        print(f"Invalid input: expected {expected_type.__name__}")
        return None
