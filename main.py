from validator import (
    validate_emergency_type,
    validate_severity,
    validate_location
)

from emergency_handler import process_emergency
from response_simulator import simulate_response
from sos_system import generate_sos_alert, display_sos_alert
from incident_manager import save_incident, get_incidents

def activate_sos():
    print("\n===== EMERGENCY SOS SIMULATOR =====")

    emergency_type = input(
        "Enter emergency type (Medical/Fire/Police/Accident): "
    ).title()

    severity = input(
        "Enter severity (Low/Medium/High/Critical): "
    ).title()

    location = input("Enter your location: ").strip()

    if not validate_emergency_type(emergency_type):
        print("invalid emergency type.")
        return
    if not validate_severity(severity):
        print("invalid severity level.")
        return
    if not validate_location(location):
        print("location cannot be empty.")
        return

    emergency = process_emergency(
        emergency_type,
        severity,
        location
    )

    response = simulate_response(emergency)

    alert = generate_sos_alert(
        emergency,
        response
    )

    display_sos_alert(alert)

    save_incident(alert)

    print("incident saved successfully.")


def view_history():
    print("\n===== INCIDENT HISTORY =====")

    incidents = get_incidents()

    if not incidents:
        print("No incidents found.")
        return

    for number, incident in enumerate(incidents, start=1):
        print(f"\nIncident {number}")
        print("Emergency Type :", incident["emergency_type"])
        print("Severity       :", incident["severity"])
        print("Location       :", incident["location"])
        print("Response Unit  :", incident["response_unit"])
        print("Response Time  :", str(incident["response_time"]) + "minutes")
        print("Status         :", incident["status"])

def main():
    while True:
        print("\n===== EMERGENCY SOS SIMULATOR =====")
        print("1. Activate SOS")
        print("2. View incident history")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            activate_sos()

        elif choice == "2":
            view_history()

        elif choice == "3":
            print("Exiting Emergency SOS Simulator.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__== "__main__":
 main()             

