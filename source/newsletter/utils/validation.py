import re 

def validate_credentials(email: str, first_name: str, last_name: str) -> bool:
    """
    Validates the credentials of the subscriber
    """
    if not email or not first_name or not last_name:
        return False
    
    if not is_valid_email(email):
        return False
    
    if not is_valid_name(first_name) or not is_valid_name(last_name):
        return False

    return True

def is_valid_name(name: str) -> bool:
    pattern = r'^[a-zA-Z]{2,}$'

    return re.match(pattern, name) is not None

def is_valid_email(email: str) -> bool: 
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return re.match(pattern, email) is not None