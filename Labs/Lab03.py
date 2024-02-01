class Shopper:
    # Class variables
    prices = {'apple': 1.99, 'bread': 2.19, 'milk': 4.96, 'pepper': 1.25}
    sale_items = ['pepper', 'banana']
    credit_threshold = 6
    default_price = 2.50
    volume_discount = 0.9
    sales_discount = 0.85

    def __init__(self, name, money):
        # Instance variables
        self.name = name
        self.money = money
        self.purchases = []

    @classmethod
    def price_list(cls):
        return cls.prices

    @classmethod
    def sale_items_list(cls):
        return cls.sale_items

    def purchase(self, items):
        total_cost = 0
        for item in items:
            price = self.prices.get(item, self.default_price)
            if item in self.sale_items:
                price *= self.sales_discount
            self.purchases.append((item, price))
            total_cost += price

        if total_cost > self.credit_threshold:
            total_cost *= self.volume_discount
            self.money -= total_cost

    def __str__(self):
        purchases_str = "\n  ".join([f"('{item}', {price:.2f})" for item, price in self.purchases])
        return f"{self.name} cash in hand ${self.money:.2f}\n  items:\n  {purchases_str}"

# Test Harness
print(f'Price dict: {Shopper.price_list()}')
print(f'Sales list: {Shopper.sale_items_list()}')

nar = Shopper('Narendra', 20)     # Create a shopper object
print(f'\n{nar}')                 # Display the object

items = 'bread milk'.split()      # List of items to buy
print(f'\n{nar.name} is purchasing: {items}')
nar.purchase(items)               # Buy the items
print(f'{nar}')                   # Display the object

items = 'apple pepper cauliflower'.split()
print(f'\n{nar.name} is purchasing: {items}')
nar.purchase(items)
print(f'{nar}')                   # Display the object

# Verification
members = [member for member in dir(Shopper) if not member.startswith('_')]
print(f'\nPublic members of the class: {members}')
properties = [member for member in members if not callable(getattr(Shopper, member))]
print(f'Public properties: {properties}')
methods = [member for member in members if callable(getattr(Shopper, member))]
print(f'Public methods: {methods}')
