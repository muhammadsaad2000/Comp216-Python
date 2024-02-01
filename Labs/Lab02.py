class Pizza:
    # Class attributes
    valid_sizes = {'small', 'medium', 'large', 'x-large'}
    prices = {'small': 6.49, 'medium': 8.49, 'large': 10.49, 'x-large': 13.49}

    # Constructor
    def __init__(self, size='medium', toppings=['cheese']):
        self._size = size
        self._toppings = toppings

    # Instance methods
    def add_toppings(self, toppings):
        self._toppings.extend(toppings)

    def __str__(self):
        return f'{self._size} pizza with {self._toppings} for ${self.price:.2f}'

    # Instance Properties
    @property
    def price(self):
        base_price = self.prices[self._size]
        toppings_cost = len(self._toppings) * 0.50
        return base_price + toppings_cost

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value.lower() not in self.valid_sizes:
            raise ValueError(f'ERROR: {value} is not a valid size for a pizza')
        self._size = value.lower()

    @property
    def toppings(self):
        return self._toppings

    @toppings.setter
    def toppings(self, value):
        if not isinstance(value, list):
            raise ValueError('Toppings must be provided as a list')
        self._toppings = value

# Test harness
print(f'Creating a default pizza')
p = Pizza()
print(p)

toppings = 'cheese olive'.split()
print(f'\nAdding topping: {toppings}')
p.add_toppings(toppings=toppings)
print(p)

print(f'\nCreating a new pizza')
p = Pizza('large', 'cheese pepper'.split())
print(p)

toppings = ['pineapple', 'mushroom']
print(f'\nAdding topping: {toppings}')
p.add_toppings(toppings)
print(p)

size = 'x-large'
p.size = size
print(f'\nChanging order size to {size}')
print(p)

size = 'gigantic'
print(f'\nChanging order size to {size}')
try:
    p.size = size
except ValueError as err:
    print(err)
