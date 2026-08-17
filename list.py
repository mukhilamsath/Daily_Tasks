squares = []

for i in range(1, 11):
    squares.append(i ** 2)

print(squares)

squares = [i ** 2 for i in range(1, 11)]

print(squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print(even_numbers)