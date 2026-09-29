from config import RESPONSE_UNITS

def process_emergency(emergency_type, severity, location):
    response_unit = RESPONSE_UNITS[emergency_type]

    emergency = {
        "type": emergency_type,
        "severity": severity,
        "location": location,
        "response_unit": response_unit
    }

    return emergency
