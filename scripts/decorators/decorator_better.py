from functools import wraps

def show_call(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        print(f"{func.__name__} called with args: {args}, kwds: {kwds}")
        return func(*args, **kwds)
    return wrapper

@show_call
def sum_numbers(*numbers, start=0):
    """Sum a list of numbers with an optional starting value."""
    return sum(numbers) + start

# Example usage
result = sum_numbers(1, 2, 3, start=10)
print(f"Result: {result}")

result_second = sum_numbers(3,5,7,start=50)
print(f"Result_Second: {result_second}")
