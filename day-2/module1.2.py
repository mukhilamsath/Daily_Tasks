
is_even = lambda x: x % 2 == 0

print(is_even(10))

is_palindrome = lambda text: text == text[::-1]

print(is_palindrome("level"))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x * x, numbers))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original:", numbers)
print("Squares:", squares)
print("Even numbers:", even_numbers)