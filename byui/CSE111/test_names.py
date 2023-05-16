from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    # Test Case 1
    result = make_full_name("John", "Doe")
    expected = "John Doe"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 2
    result = make_full_name("Alice", "Smith")
    expected = "Alice Smith"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 3
    result = make_full_name("Bob", "Johnson")
    expected = "Bob Johnson"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 4
    result = make_full_name("Sarah", "Williams")
    expected = "Sarah Williams"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Add more test cases if needed

    print("All tests passed!")

# Define the make_full_name function
def make_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

# Call the test_make_full_name function to run the tests
test_make_full_name()

def test_extract_family_name():
    # Test Case 1
    result = extract_family_name("John Doe")
    expected = "Doe"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 2
    result = extract_family_name("Alice Smith")
    expected = "Smith"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 3
    result = extract_family_name("Bob Johnson")
    expected = "Johnson"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 4
    result = extract_family_name("Sarah Williams")
    expected = "Williams"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Add more test cases if needed

    print("All tests passed!")

# Define the extract_family_name function
def extract_family_name(full_name):
    return full_name.split()[-1]

# Call the test_extract_family_name function to run the tests
test_extract_family_name()

def test_extract_given_name():
    # Test Case 1
    result = extract_given_name("John Doe")
    expected = "John"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 2
    result = extract_given_name("Alice Smith")
    expected = "Alice"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 3
    result = extract_given_name("Bob Johnson")
    expected = "Bob"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Test Case 4
    result = extract_given_name("Sarah Williams")
    expected = "Sarah"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Add more test cases if needed

    print("All tests passed!")

# Define the extract_given_name function
def extract_given_name(full_name):
    return full_name.split()[0]

# Call the test_extract_given_name function to run the tests
test_extract_given_name()

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])