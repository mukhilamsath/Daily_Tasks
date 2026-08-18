from functools import wraps


def mydecorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Before function call")

        result = function(*args, **kwargs)

        print("After function call")

        return result

    return wrapper


@mydecorator
def greet():
    print("heloooo")


print(greet.__name__)

greet()