class Pizza:
    def __init__(self, size, topping):
        self.size = size
        self.top = topping
    def eat(self):
        print(f"Nom nom! Eating a {self.size} pizza loaded with {self.top}!")


my_pizza = Pizza("Large", "extra souce")
my_pizza.eat()