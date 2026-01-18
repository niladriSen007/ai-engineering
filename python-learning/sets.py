large = set(range(1000))
small = set(range(500, 1500))

print("Large set size:", len(large))
print("Small set size:", len(small))
intersection = large & small
print("Intersection size:", intersection)


num1 = {1, 2, 3}
num1.update({4, 5, 6})
print("Updated num1 set:", num1)


data = [{"name": "Alice", "age": 30}, {"name": "Bob"}, {"name": "Charlie", "age": 25}]

for entry in data:
    age = entry.get("age", "Age not provided")
    print(f"{entry['name']} is {age} years old.")
