import datetime

def calculate_total(subtotal):
    discount = 0
    if today.weekday() in [1, 2] and subtotal >= 50:
        discount = subtotal * 0.10
        subtotal -= discount
    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax
    if discount > 0:
        print("Discount amount: $%.2f" % discount)
    print("Sales tax: $%.2f" % sales_tax)
    print("Total amount due: $%.2f" % total)
    if discount == 0 and today.weekday() in [1, 2]:
        additional_purchase = 50 - subtotal
        print("Additional purchase needed for discount: $%.2f" % additional_purchase)

today = datetime.datetime.today()

subtotal = 0
while True:
    price = float(input("Enter price (0 to quit): "))
    if price == 0:
        break
    quantity = int(input("Enter quantity: "))
    subtotal += price * quantity

print("Subtotal: $%.2f" % subtotal)
calculate_total(subtotal)