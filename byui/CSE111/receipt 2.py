import csv
import datetime

STORE_NAME = "Chris's Market"
SALES_TAX_RATE = 0.06

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename (str): The name of the CSV file to read.
        key_column_index (int): The index of the column
            to use as the keys in the dictionary.

    Returns:
        dict: A compound dictionary that contains the contents of the CSV file.
    """
    compound_dict = {}

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[key_column_index]
            values = row
            compound_dict[key] = values

    return compound_dict

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)
        print(STORE_NAME)
        print("Receipt")
        print("---------------------------")
        print()

        ordered_items = []
        subtotal = 0

        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first line
            for row in reader:
                try:
                    product_number = row[0]
                    quantity = int(row[1])
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    product_price = float(product_info[2])
                    item_total = product_price * quantity
                    ordered_items.append((product_name, quantity, product_price, item_total))
                    subtotal += item_total
                except KeyError:
                    print(f"Product number {product_number} not found. Skipping...")

        print("Ordered Items:")
        for item in ordered_items:
            product_name, quantity, product_price, item_total = item
            print(f"{product_name} - Quantity: {quantity} - Price: ${product_price:.2f} - Total: ${item_total:.2f}")
        print()

        print(f"Number of Ordered Items: {len(ordered_items)}")
        print(f"Subtotal: ${subtotal:.2f}")
        sales_tax = subtotal * SALES_TAX_RATE
        total_due = subtotal + sales_tax
        print(f"Sales Tax (6%): ${sales_tax:.2f}")
        print(f"Total Due: ${total_due:.2f}")
        print()

        # Print coupon
        if ordered_items:
            product_name, _, _, _ = ordered_items[0]
            print("Coupon:")
            print(f"10% off your next purchase of {product_name}!")

        print("Thank you for shopping with us!")
        current_datetime = datetime.datetime.now()
        print(f"Date and Time: {current_datetime}")
         # Print survey invitation
        print()
        print("Please take a moment to complete our online survey:")
        print("www.chris'smarket.com/survey")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except KeyError as e:
        print(f"Error: Key '{e.args[0]}' not found.")

if __name__ == '__main__':
    main()