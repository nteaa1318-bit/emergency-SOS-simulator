from config import EMERGENCY_TYPES, SEVERITY_LEVELS

def validate_emergency_type(emergency_type):
    if emergency_type not in EMERGENCY_TYPES:
        return False
    return True

def validate_severity(severity):
    if severity not in SEVERITY_LEVELS:
        return False
    return True

def validate_location(location):
    if not location.strip():
        return False
    return True
