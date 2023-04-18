manufactured_items = int(input("Enter the number of manufactured items: "))
items_per_box = int(input("Enter the number of items to pack per box: "))

num_boxes = manufactured_items // items_per_box
if manufactured_items % items_per_box != 0:
    num_boxes += 1

print("The number of boxes necessary is:", num_boxes)