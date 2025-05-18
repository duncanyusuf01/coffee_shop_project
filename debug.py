from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Yusuf")
c2 = Customer("Victor")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

Order(c1, latte, 5.0)
Order(c1, latte, 6.5)
Order(c2, latte, 3.5)
Order(c2, espresso, 4.0)

print("--- Orders for Yusuf ---")
for order in c1.orders():
    print(f"{order.coffee.name}: ${order.price}")

print("\n--- Coffees Yusuf Ordered ---")
for coffee in c1.coffees():
    print(coffee.name)

print("\n--- Average Price of Latte ---")
print(latte.average_price())

print("\n--- Most Aficionado for Latte ---")
print(Customer.most_aficionado(latte).name)
