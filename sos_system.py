def generate_sos_alert(emergency, response):
    alert = {
        "message": "SOS ALERT ACTIVATED",
        "emergency_type": emergency["type"],
        "severity": emergency["severity"],
        "location": emergency["location"],
        "response_unit": response["response_unit"],
        "response_time": response["response_time"],
        "status": response["status"]
    }

    return alert

def display_sos_alert(alert):
    print("\n=======SOS ALERT=======")
    print(alert["message"])
    print("----------------------")
    print("Emergency Type :", alert["emergency_type"])
    print("Severity       :",alert["severity"])
    print("Location       :", alert["location"])
    print("Response Unit  :", alert["response_unit"])
    print("Resonse Time   :", str(alert["response_time"]) + "minutes")
    print("Status         :", alert["status"])
    print("=======================\n")
    