# Storage Design

## Storage Method

The Emergency SOS Simulator uses a JSON filr for storing incident history.

## Storage Location

All incidents records are stored in:

`data/incidents.json`

## Stored Information

Each incident record contains:

- Emergency Type
- Severity
- Location
- Response Unit
- Response Time
- Status

## Saving Data

The `incident_manager.py` module saves each completed SOS incident to the JSON file.

When a new incident is created, it is added to the existing incident records.

## Retrieving Data

The `incident_manager.py` module reads the JSON file whenever the user selects **View Incident History**.

The stored incidents are then displayed through the main program.

## Data Format

The information is stored as a list of JSON objects, making it simple to read, update, and maintain.

## Error Handling

If the storage files does not exist, the system starts with an empty incident history.

If the JSON file contains invalid data, the system safely handles the error and returns an empty incident list.