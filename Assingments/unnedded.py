def is_valid_10_digits(user_input):
    """
    Checks if the input is exactly 10 digits long and contains only digits.
    
    Args:
        user_input: The input to validate
        
    Returns:
        bool: True if input is exactly 10 digits, False otherwise
    """
    return user_input.isdigit() and len(user_input) == 10