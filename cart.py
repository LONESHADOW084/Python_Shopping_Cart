class Item:
    def __init__(self, name,price):
        self.name = name
        self.price = price
        self.quantity = 0

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        item_quantity += quantity
        self.items.append(item)

    def remove_item(self, item):
        self.ietms.remove(item)
        item.quantity = 0

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items:
                total_price += item.price * item.quantity
                print(f"{item.name} (Quantity: {item.quantity}, Price: ${item.price})")
            print(f"Total Price: ${total_price}")

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Unable to checkout. Although you can leave not so suspiously.")
        else:
            total_price = 0
            print("Reciept:")
            for item in self.items:
                total_price += item.price * item.quantity
                print(f"{item.name} (Quantity: {item.quantity}, Price: ${item.price})")
            print(f" Total Price: ${total_price}")

    def shopping_cart_program():
        cart = ShoppingCart()
        while True:
            print("\n--- Walmart ---")
            print("1. Add item to cart")
            print("2. Remove item from cart")
            print("3. View cart")
            print("4. Checkout")
            print("5. Run out of store (Quit)")
            choice = input("Enter your choice:")

            if choice == "1":
                name = input("Enter item name:")
                price = float(input("Enter item price:"))
                quantity = int(input("Enter item quantity:"))
                item = Item(name, price)
                cart.add_item(item, quantity)
                print(f"{quantity} {name}(s) added to cart.")

            elif choice == "2":
                cart.view_cart()
                if cart.items:
                    item_name = input("Enter the name of the item to remove:")
                    for item in cart.items:
                        if item.name == item_name:
                            cart.remove_item(name)
                            print (f"{item.name} removed from the cart. Why don't you want it?")
                            break
                    else:
                        print(f"{item.name} is not in the cart. You probably dropped it back there.")

            elif choice == "3":
                cart.view_cart()
                
            elif choice == "4":
                cart.checkout()
                break

            elif choice == "5":
                print("Hey come back here! Security! We have a runner.")

            else:
                print("Invalid. Please try again.")
