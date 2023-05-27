# sabad kharid
# sabad kharid
class Product:
    def init(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def init(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append((product, quantity))

    def remove_item(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            product, quantity = item
            total += product.price * quantity
        return total

# product1 = Product(" iphone 13", 10)
# product2 = Product(" acer pradator ", 5)
# product3 = Product(" keyboard ", 2)

# cart = ShoppingCart()
# cart.add_item(product1, 2)
# cart.add_item(product2)
# cart.add_item(product3, 3)
# cart.remove_item(product2)

total_price = cart.calculate_total()

print("total : ", total_price)