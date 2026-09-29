import json
import os

FILE_PATH = "data/incidents.json"

def save_incident(incident):
    os.makedirs("data", exist_ok=True)

    incidents = []

    if os.path.exists(FILE_PATH):
     with open(FILE_PATH, "r") as file:
        try:
            incidents = json.load(file)
        except json.JSONDecodeError:
            incidents = []

    incidents.append(incident)

    with open(FILE_PATH, "w") as file:
        json.dump(incidents, file, indent=4)

def get_incidents():
   if not os.path.exists(FILE_PATH):
      return []

   with open(FILE_PATH, "r") as file:
      try:
         return json.load(file)
      except json.JSONDecodeError:
         return []
              

 