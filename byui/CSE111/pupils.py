import csv

# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter:
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(lst, title):
    """Print each element of the list on a separate line with a title.

    Parameters:
        lst: the list to print
        title: the title of the list
    """
    print(f"Ordered by {title}:")
    for element in lst:
        print(element)
    print()

def main():
    # Call the read_compound_list function to read the pupils.csv file into a list named students_list.
    students_list = read_compound_list("pupils.csv")

    # Write a lambda function that will extract the birthdate from a student.
    extract_birthdate = lambda student: student[BIRTHDATE_INDEX]

    # Sort the students_list by birthdate from oldest to youngest.
    sorted_by_birthdate = sorted(students_list, key=extract_birthdate)

    # Print the students_list ordered by birthdate.
    print_list(sorted_by_birthdate, "Oldest to Youngest")

    # Write a lambda function that will extract the given name from a student.
    extract_given_name = lambda student: student[GIVEN_NAME_INDEX]

    # Sort the students_list by given name.
    sorted_by_given_name = sorted(students_list, key=extract_given_name)

    # Print the students_list ordered by given name.
    print_list(sorted_by_given_name, "Given Name")

    # Write a lambda function that will extract the birth month and day from a student's birthdate.
    extract_birth_month_day = lambda student: student[BIRTHDATE_INDEX].split('-')[1:]

    # Sort the students_list by birth month and day.
    sorted_by_birth_month_day = sorted(students_list, key=extract_birth_month_day)

    # Print the students_list ordered by birth month and day.
    print_list(sorted_by_birth_month_day, "Birth Month and Day")

# Call the main function to execute the program.
main()