import csv

def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first line
        for row in reader:
            if len(row) > key_column_index:
                key = row[key_column_index]
                value = row[1 - key_column_index]
                dictionary[key] = value
    return dictionary

def main():
    filename = 'students.csv'
    key_column_index = 0

    # Read the dictionary from the CSV file
    dictionary = read_dictionary(filename, key_column_index)

    # Get I-Number from the user
    i_number = input("Enter I-Number: ")

    # Check if the I-Number exists in the dictionary and print the corresponding name
    if i_number in dictionary:
        name = dictionary[i_number]
        print("Name:", name)
    else:
        print("No such student")

# Run the main function
if __name__ == '__main__':
    main()