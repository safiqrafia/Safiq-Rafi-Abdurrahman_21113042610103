
menu = ("crab legs", "ice cream", "pizza", "burger", "pasta")

print("The Buffet menu is:")
for food in menu:
    print(food)

try:
    menu[0] = "new value"
except TypeError:
    print("\nSorry, the menu can't be changed!\n")

new_menu = ("crab legs", "ice cream", "pizza", "salad", "soup")

print("The new/revised Buffet menu is:")
for food in new_menu:
    print(food)