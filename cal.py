class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to the cart.")

    def display_cart(self):
        if self.items:
            print("Items in the cart:")
            for item in self.items:
                print("-", item)
        else:
            print("Your cart is empty.")