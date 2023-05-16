import pytest
from address import extract_city, extract_state, extract_zipcode

def test_extract_city():
    # Test Case 1
    result = extract_city("New York, USA")
    expected = "New York"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 2
    result = extract_city("London, United Kingdom")
    expected = "London"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 3
    result = extract_city("Paris, France")
    expected = "Paris"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 4
    result = extract_city("Tokyo, Japan")
    expected = "Tokyo"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Add more test cases if needed

    print("All tests passed!")


def test_extract_state():
    # Test Case 1
    result = extract_state("New York, USA")
    expected = "USA"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 2
    result = extract_state("London, United Kingdom")
    expected = "United Kingdom"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 3
    result = extract_state("Paris, France")
    expected = "France"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 4
    result = extract_state("Tokyo, Japan")
    expected = "Japan"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Add more test cases if needed

    print("All tests passed!")


def test_extract_zipcode():
    # Test Case 1
    result = extract_zipcode("New York, USA 10001")
    expected = "10001"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 2
    result = extract_zipcode("London, United Kingdom SW1A 1AA")
    expected = "SW1A 1AA"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 3
    result = extract_zipcode("Paris, France 75000")
    expected = "75000"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 4
    result = extract_zipcode("Tokyo, Japan 100-0000")
    expected = "100-0000"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Add more test cases if needed

    print("All tests passed!")


if __name__ == "__main__":
    test_extract_city()
    test_extract_state()
    test_extract_zipcode()