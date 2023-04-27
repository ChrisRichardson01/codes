from datetime import datetime

def main():
    while True:
        # Get the user's gender, birthdate, height, and weight.
        gender = input("Enter your gender (M/F): ").strip().lower()
        if gender not in ['m', 'f']:
            print("Invalid gender. Please enter 'M' or 'F'.")
            continue
        birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ").strip()
        if birthdate_str == "exit":
            return
        try:
            weight_lb = float(input("Enter your weight in pounds: ").strip())
        except ValueError:
            print("Invalid weight. Please enter a number.")
            continue
        try:
            height_in = float(input("Enter your height in inches: ").strip())
        except ValueError:
            print("Invalid height. Please enter a number.")
            continue

        # Call the compute_age, kg_from_lb, ft_in_to_cm,
        # body_mass_index, and basal_metabolic_rate functions
        # as needed.
        age = compute_age(birthdate_str)
        weight_kg = kg_from_lb(weight_lb)
        feet = int(height_in // 12)
        inches = height_in % 12
        height_cm = ft_in_to_cm(feet, inches)
        bmi = body_mass_index(weight_kg, height_cm)
        bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

        # Print the results for the user to see.
        print(f"Age: {age} years")
        print(f"Weight: {weight_lb:.2f} pounds = {weight_kg:.2f} kg")
        print(f"Height: {height_in:.2f} inches = {height_cm:.2f} cm")
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

def ft_in_to_cm(feet, inches):
    """Convert a height in feet and inches to centimeters.
    Parameters
        feet: a height in feet.
        inches: a height in inches.
    Return: the height in centimeters.
    """
    return (feet * 12 + inches) * 2.54

def body_mass_index(weight_kg, height_cm):
    """Calculate and return the body mass index (BMI) for a person.
    Parameters
        weight_kg: a person's weight in kilograms.
        height_cm: a person's height in centimeters.
    Return: the person's BMI.
    """
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def basal_metabolic_rate(gender, weight_kg, height_cm, age):
    """Calculate and return a person's basal metabolic rate (BMR).
    Parameters
        gender: a string representing the person's gender ('m' or 'f').
        weight_kg: a person's weight in kilograms.
        height_cm: a person's height in centimeters.
        age: a person's age in years.
    Return: the person's BMR in kilocalories per day.
    """
    if gender == 'm':
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    return bmr

if __name__ == '__main__':
    main()