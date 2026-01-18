from copy import deepcopy

a, b, c = 1, 2, 3
print(a, b, c)

# swap values
a = 5
b = 6
a, b = b, a
print(a, b)

# int, float, str, and tuple. If you try to change them, a new object is created in memory.

name = "Niladri"
# name[0] = "X" // Error as strings are immutable
print(name[0])


val1 = 0.1
val2 = 0.2
print(val1 + val2)
print(round(val1 + val2, 2))


# tuples
coord = (1, 2)
x, y = coord
x = 12
print(x, y)
print(coord)
print(type(coord))


print("---------------AString Comparison----------------")
# string comparison
s1 = "aa"
s2 = "ab"
print(s1 < s2)
print(s1 == s2)
print(s1 is s2)
print(id(s1))
print(id(s2))

original = "Hi Nil"
copy = original
modified = copy.replace("Nil", "Nilesh")
print(original)
print(copy)
print(modified)

# Dictionary example
scores: dict[str, int] = {"Niladri": 10, "Nil": 20, "Nilesh": 30}
updated_scores = {name: score + 5 for name, score in scores.items()}
print(updated_scores)


print("------------------List------------------")
# list
l1 = ["banana", "apple", "axe", "cherry"]
l2 = sorted(l1)
print(l1)
l1.sort(key=len)
print(l1)
print(l2)


print("--------------------Copying------------------")
# shallow copy
l4 = [1, [2, 3], 4, 5]
l5 = l4.copy()
l6 = deepcopy(l4)
l5[0] = 10
print(f"Before shallow copy: {l4}")
print(f"After shallow copy: {l5}")
l6[0] = 10
print(f"Before deep copy: {l4}")
print(f"After deep copy: {l6}")
l5[1][0] = 4577
print(f"After shallow copy: {l4}")
print(f"After shallow copy: {l5}")
l6[1][0] = 9988
print(f"After deep copy: {l4}")
print(f"After deep copy: {l6}")


print("------------------List Comprehension------------------")
list1 = [1, 2, 3, 5]
list2 = ["a", "b", "c", "d"]
list3 = [(x, y) for x, y in zip(list1, list2)]
print(list3)

import time

# Using a for loop
start = time.time()
squares = []
for x in range(1000000):
    squares.append(x**2)
end = time.time()
print(f"For loop time: {end - start:.5f} seconds")

# Using list comprehension
start = time.time()
squares = [x**2 for x in range(1000000)]
end = time.time()
print(f"List comprehension time: {end - start:.5f} seconds")


# flatten a multidimensional array
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for arr in matrix for item in arr]
print(flattened)

# Creating a New Nested List
grid_size = 3
mat = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
print(mat)


# ashok chakraborty

# 8879611275
# 7021411275
