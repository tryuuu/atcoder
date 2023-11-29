from itertools import product

n, p, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_price = 0

# Generate all possible combinations of main and side dishes
for main_dish, side_dish in product(a, b):
    s = main_dish + side_dish
    set_meal_price = min(s, p)
    total_price += set_meal_price

print(total_price)
