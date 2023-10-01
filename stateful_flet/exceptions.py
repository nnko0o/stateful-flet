class StateValueError(ValueError):
    '''
    Simple Exception for ValueError in statfuly Objects
    This will you got when you enter value with wrong type
    '''
    def __init__(self, error_type, state_type):
        super().__init__(
            f"[StateValueError]: You Enter `{error_type}` But The State Is `{state_type}`"
        )