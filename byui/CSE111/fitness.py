from datetime import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender (M/F): ")
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    weight_lb = float(input("Enter your weight in pounds: "))
    height_in = float(input("Enter your height in inches: "))

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthdate_str)
    weight_kg = kg_from_lb(weight_lb)
    height_cm = cm_from_in(height_in)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    # Print the results for the user to see.
    print(f"Age: {age} years")
    print(f"Weight: {weight_kg:.2f} kg")
    print(f"Height: {height_cm:.2f} cm")
    print(f"BMI: {bmi:.2f}")
    print(f"BMR: {bmr:.2f} kcals per day")

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return pounds * 0.45359237

def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return inches * 2.54

def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return weight / (height / 100) ** 2

def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        gender: a string representing the person's gender ("M" for male, "F" for female).
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == "M":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    elif gender == "F":
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    else:
        raise ValueError("Gender must be 'M' or 'F'.")

    return bmr

if __name__ == 'main':
    main()