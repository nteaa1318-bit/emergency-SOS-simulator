import random 

def simulate_response(emergency):
    response_times = {
        "Low": (10,20),
        "Medium": (7,15),
        "High": (4,10),
        "Critical": (2,6)
    }

    severity = emergency["severity"]
    minimum, maximum = response_times[severity]

    response_time = random.randint(minimum, maximum)

    result = {
        "response_unit": emergency["response_unit"],
        "response_time":response_time,
        "status": "Response Dispatched"
    }

    return result
