# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def extract_city(full_address):
    """
    Extract and return the name of a city from a properly formatted U.S. mailing address.
    
    Parameters:
        full_address (str): A U.S. mailing address in this format: number and street, city, state zipcode
    
    Returns:
        str: The city name
    """
    full_address = full_address.strip()
    last_comma_index = full_address.rindex(",") if "," in full_address else len(full_address)
    mid_comma_index = full_address.rfind(",", 0, last_comma_index)
    city = full_address[mid_comma_index + 1 : last_comma_index]
    city = city.strip()
    return city


def extract_state(full_address):
    """
    Extract and return the two-letter abbreviation for a state from a properly formatted U.S. mailing address.
    
    Parameters:
        full_address (str): A U.S. mailing address in this format: number and street, city, state zipcode
    
    Returns:
        str: The two-letter state abbreviation
    """
    full_address = full_address.strip()
    last_comma_index = full_address.rindex(",") if "," in full_address else -1
    last_space_index = full_address.rindex(" ") if " " in full_address else -1
    state = ""
    if last_comma_index != -1 and last_space_index != -1:
        state = full_address[last_comma_index + 1 : last_space_index].strip()
    return state


def extract_zipcode(full_address):
    """Extract and return the ZIP code from
    a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the ZIP code
    """
    full_address = full_address.strip()
    last_space_index = full_address.rindex(" ")
    zipcode = full_address[last_space_index + 1 : ]
    return zipcode
