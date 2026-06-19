#PROJECT 2: Smart Grocery System (Lists + Add/Remove + Logic)
#🎯 What you will build:

#A mini grocery management system.
#You must:
#Print cart items
#Add 2 new items from user input
#Remove 1 item (user choice)
#Replace one item with something new
#Print final cart

#🔥 Extra Challenge:

#If cart has more than 4 items:
#👉 print "Cart is full"

#Else:
#👉 print "You can still add items"

print("grocery management system")


print("print Cart items")
# start with a sample cart
cart = ["milk", "eggs", "bread"]

print("\nCurrent Cart:")

for item in cart:
    print("-", item)
# Add 2 new items from user input
item1 = input("Add item 1: ")
item2 = input("Add item 2: ")
item3 = input("Add item 3:")
cart.append(item1)
cart.append(item2)
cart.append(item3)

print("Cart after additions:", cart)

# Remove 1 item (user choice)
to_remove = input("Enter an item to remove: ")
if to_remove in cart:
	cart.remove(to_remove)
	print(f'Removed {to_remove}')
else:
	print(f'{to_remove} not in cart')

# Replace one item with something new
old_item = input("Enter an item to replace: ")
new_item = input("Enter the new item: ")
if old_item in cart:
	idx = cart.index(old_item)
	cart[idx] = new_item
	print(f'Replaced {old_item} with {new_item}')
else:
	print(f'{old_item} not in cart to replace')

print("Final cart:", cart)

# Extra challenge: check cart size
if len(cart) > 4:
	print("Cart is full")
else:
	print("You can still add items")
