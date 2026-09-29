# Emergency SOS Simulator

## Project Overview

Emergency SOS Simulator is a Python-based simulation project designed to demonstrate how an emergency alert workflow can be handled through a modular software system.

The simulator accepts emergency information from the user, validates the input, processes the emergency, simulates an appropriate response, generates an SOS alert, and stores theincident for later viewing.

## Problem Statement

During an emergency, important information such as the type of emergency, severity, and location needs to be communicated clearly and processed quikly.

This project provides a simulated emergency workflow that demonstrates how such information can be collected, validated, processed, ans stored using python

## objectives

- Collect emergency information from the user.
- Validate emergency type, severity, and location.
- Process emergency information using seperate modules.
- Simulate an appropriate emergency response.
- Generate an SOS alert.
- Store emergency incidents.
- Allow users to view incident history.
- Test input validation using automated tests.

## Features

- Emergency type selection
- Severity selection
- Location input
- Input validation
- Emergency response simulation
- SOS alert generation
- Incident storage using JSON
- Incident history
- Menu-driven interface
- Automated validation tests

## Technologies used

- Python
- JSON
- Pytest
- Visual studio code

## Project structure

```text
emergency_SOSsimulator/
|
|--data/
|    |--incidents.json
|
|--tests/
|     |-- test_sos.py
|
|--config.py
|--emergency_handler.py
|--incident_manager.py
|--main.py
|--response_simulator.py
|--sos_system.py
|--validator.py
|--README.md
|--statement.md

