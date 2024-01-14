""" 
Create a Product class and a Shop class.
Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not.
If you successfully buy a product, then throw a Congress message.
"""

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def sell_product(self, quantity):
        self.quantity -= quantity

    def __repr__(self) -> str:
        return f"{self.name} (x{self.quantity}) -> {self.price}/-"

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity, price):
        if (price < 1) or (quantity < 1):
            print(f"Invalid price or quantity, '{name}' was not added to the shop")
        else:
            new_product = Product(name, quantity, price)
            self.products.append(new_product)
            print(f"{name}(x{quantity}) was added to the shop")

    def buy_product(self, name, quantity):
        found = False
        for product in self.products:
            if product.name == name:
                found = True
                while product.quantity < quantity:
                    print(f"Sorry! we only have {product.quantity} {name} in stock!")
                    print("Want to buy a lower valid amount? [Enter 0 if you want to cancel this purchase]")
                    quantity = int(input("Entry: "))
                if quantity > 0:
                    product.sell_product(quantity)
                    print(f"Congratulation! you just bought {name}(x{quantity}) for {product.price * quantity} Tk.")
                    if(product.quantity == 0): self.products.remove(product)
                break
        if found is False:
            print(f"Sorry! we don't have {name} right now")

    def show_products(self):
        if len(self.products) == 0:
            print("Oops! There are no products yet! Please add some.")
        else:
            counter = 1
            print("Available Products:")
            for product in self.products:
                print(counter,':',product)
                counter += 1

print("------------------------------")
print("Welcome to Terminal Supershop!")
customer = Shop()
while True:
    print("------------------------------")
    print("  What would you like to do?")
    print("    Show Products [Enter 3]")
    print("    Buy  Product  [Enter 2]")
    print("    Add  Product  [Enter 1]")
    print("    Leave Shop!   [Enter 0]")
    print("------------------------------")
    choice = input("Entry: ")
    if choice == "0":
        print("Thanks for visiting Terminal Supershop. Come again")
        break
    
    if choice == "1":
        pro_name = input("Enter the Name of product you want to add: ")
        pro_price = input(f"Enter the Price of each {pro_name}: ")
        pro_quantity = input(f"Enter how Many {pro_name} would you add: ")
        customer.add_product(pro_name, int(pro_quantity), int(pro_price))

    elif choice == "2":
        product = input("Enter the Name of product you want to buy: ")
        amount = input(f"Enter how Many {product} you want to buy: ")
        customer.buy_product(product, int(amount))

    elif choice == "3":
        customer.show_products()

    else:
        print("Invalid Activity!")
    
