def find_min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

        if number > maximum:
            maximum = number

    return minimum, maximum

def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def is_palindrome(text):
    return text == text[::-1]

numbers = [10, 25, 7, 42, 18]

minimum, maximum = find_min_max(numbers)
average = calculate_average(numbers)
prime =  is_prime(17)
palindrome = is_palindrome("radar")
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
print("prime or not :", prime)
print("palindrome or not :", palindrome)