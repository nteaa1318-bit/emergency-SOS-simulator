from validator import (
    validate_emergency_type,
    validate_severity,
    validate_location
)

def test_valid_emergency_type():
    assert validate_emergency_type("Medical") is True

def test_invalid_emergency_type():
    assert validate_emergency_type("Unknown") is False

def test_valid_severity():
    assert validate_severity("Critical") is True

def test_invalid_severity():
    assert validate_severity("Extreme") is False

def test_valid_location():
    assert validate_location("VIT Bhopal") is True

def test_empty_location():
    assert validate_location("") is False
                   
