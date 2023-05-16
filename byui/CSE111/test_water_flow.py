from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

def test_water_column_height():
    test_cases = [
        (0, 0, 0),
        (0, 10, 7.5),
        (25, 0, 25),
        (48.3, 12.8, 57.9)
    ]

    for tower_height, tank_height, expected_height in test_cases:
        result = water_column_height(tower_height, tank_height)
        print(f"Tower Height: {tower_height}, Tank Wall Height: {tank_height}")
        print(f"Expected Water Column Height: {expected_height}")
        print(f"Calculated Water Column Height: {result}")
        print("-------------------------")

test_water_column_height()

def test_pressure_gain_from_water_height():
    test_cases = [
        (0, 0),
        (30.2, 295.628),
        (50, 489.450)
    ]

    tolerance = 0.001

    for height, expected_pressure in test_cases:
        result = pressure_gain_from_water_height(height)
        diff = abs(result - expected_pressure)
        print(f"Height: {height} meters")
        print(f"Expected Pressure: {expected_pressure} kPa")
        print(f"Calculated Pressure: {result} kPa")
        print(f"Absolute Tolerance: {tolerance}")
        print(f"Result within Tolerance: {diff <= tolerance}")
        print("-------------------------")

test_pressure_gain_from_water_height()

def test_pressure_loss_from_pipe():
    test_cases = [
        (0.048692, 0, 0.018, 1.75, 0),
        (0.048692, 200, 0, 1.75, 0),
        (0.048692, 200, 0.018, 0, 0),
        (0.048692, 200, 0.018, 1.75, -113.008),
        (0.048692, 200, 0.018, 1.65, -100.462),
        (0.28687, 1000, 0.013, 1.65, -61.576),
        (0.28687, 1800.75, 0.013, 1.65, -110.884)
    ]

    tolerance = 0.001

    for diameter, length, friction, velocity, expected_loss in test_cases:
        result = pressure_loss_from_pipe(diameter, length, friction, velocity)
        diff = abs(result - expected_loss)
        print(f"Pipe Diameter: {diameter} meters")
        print(f"Pipe Length: {length} meters")
        print(f"Friction Factor: {friction}")
        print(f"Fluid Velocity: {velocity} m/s")
        print(f"Expected Pressure Loss: {expected_loss} kPa")
        print(f"Calculated Pressure Loss: {result} kPa")
        print(f"Absolute Tolerance: {tolerance}")
        print(f"Result within Tolerance: {diff <= tolerance}")
        print("-------------------------")

test_pressure_loss_from_pipe()

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])