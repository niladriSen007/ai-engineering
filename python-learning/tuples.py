coordinate = (12, 3, 4)
a, *b = coordinate
print(a)
print(b)


nested_data = ((1, 2), (3, 4), (5, 6))
((x1, y1), (x2, y2), (x3, y3)) = nested_data

print(f"Point 1: ({x1}, {y1}), Point 2: ({x2}, {y2}), Point 3: ({x3}, {y3})")
