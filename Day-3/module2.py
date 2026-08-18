
import time
from functools import wraps
def fibonacci(n):
  
    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b

def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        start_time = time.perf_counter()

        result = function(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(
            f"[timer :] {function.__name__} "
            f"took {execution_time:.6f} seconds"
        )
        return result
    
    return wrapper



def logger(function):
 
    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"Function: {function.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")

        result = function(*args, **kwargs)

        return result

    return wrapper




@timer
@logger
def find_max(numbers):

    maximum = numbers[0]

    for number in numbers:

        if number > maximum:
            maximum = number

    return maximum




@timer
@logger
def calculate_average(numbers):

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)




@timer
@logger
def is_palindrome(text):

    return text == text[::-1]


print("FIBONACCI")
print('\n')

for number in fibonacci(10):
    print(number)


print("maximum:")
print('\n')

numbers = [10, 25, 7, 42, 18]

result = find_max(numbers)

print("Maximum:", result)

print("average")
print('\n')


numbers = [10, 20, 30, 40, 50]

result = calculate_average(numbers)

print("Average:", result)



print("PALINDROME CHECK")
print('\n')

text = "madam"

result = is_palindrome(text)

print("Is palindrome:", result)



