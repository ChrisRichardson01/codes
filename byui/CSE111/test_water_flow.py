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

from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings

# Existing test functions...

def test_pressure_loss_from_fittings():
    test_cases = [
        (0, 3, 0, 0.001),
        (1.65, 0, 0, 0.001),
        (1.65, 2, -0.109, 0.001),
        (1.75, 2, -0.122, 0.001),
        (1.75, 5, -0.306, 0.001)
    ]

    tolerance = 0.001

    for velocity, quantity, expected_loss, approx_tolerance in test_cases:
        result = pressure_loss_from_fittings(velocity, quantity)
        diff = abs(result - expected_loss)
        print(f"Fluid Velocity: {velocity} m/s")
        print(f"Quantity of Fittings: {quantity}")
        print(f"Expected Pressure Loss: {expected_loss} kPa")
        print(f"Calculated Pressure Loss: {result} kPa")
        print(f"Absolute Tolerance: {tolerance}")
        print(f"Result within Tolerance: {diff <= tolerance}")
        print("-------------------------")

test_pressure_loss_from_fittings()

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number

# Existing test functions...

def test_reynolds_number():
    test_cases = [
        (0.048692, 0, 0, 1),
        (0.048692, 1.65, 80069, 1),
        (0.048692, 1.75, 84922, 1),
        (0.28687, 1.65, 471729, 1),
        (0.28687, 1.75, 500318, 1)
    ]

    tolerance = 1

    for diameter, velocity, expected_reynolds, approx_tolerance in test_cases:
        result = reynolds_number(diameter, velocity)
        diff = abs(result - expected_reynolds)
        print(f"Hydraulic Diameter: {diameter} meters")
        print(f"Fluid Velocity: {velocity} m/s")
        print(f"Expected Reynolds Number: {expected_reynolds}")
        print(f"Calculated Reynolds Number: {result}")
        print(f"Absolute Tolerance: {tolerance}")
        print(f"Result within Tolerance: {diff <= tolerance}")
        print("-------------------------")

test_reynolds_number()

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction

# Existing test functions...

def test_pressure_loss_from_pipe_reduction():
    test_cases = [
        (0.28687, 0, 1, 0.048692, 0, 0.001),
        (0.28687, 1.65, 471729, 0.048692, -163.744, 0.001),
        (0.28687, 1.75, 500318, 0.048692, -184.182, 0.001)
    ]

    tolerance = 0.001

    for larger_diameter, velocity, reynolds, smaller_diameter, expected_loss, approx_tolerance in test_cases:
        result = pressure_loss_from_pipe_reduction(larger_diameter, velocity, reynolds, smaller_diameter)
        diff = abs(result - expected_loss)
        print(f"Larger Diameter: {larger_diameter} meters")
        print(f"Fluid Velocity: {velocity} m/s")
        print(f"Reynolds Number: {reynolds}")
        print(f"Smaller Diameter: {smaller_diameter} meters")
        print(f"Expected Pressure Loss: {expected_loss} kPa")
        print(f"Calculated Pressure Loss: {result} kPa")
        print(f"Absolute Tolerance: {tolerance}")
        print(f"Result within Tolerance: {diff <= tolerance}")
        print("-------------------------")

test_pressure_loss_from_pipe_reduction()

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])