
def is_prime(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        if num < 2:
            return "Составное"
        for i in range(2, num):
            if num % i == 0:
                print("Составное")
            print("простое")
            return num
    return wrapper
@is_prime
def sum_three(*args):
    total = 0
    for number in args:
        total += number
    return total

result = sum_three(2, 3, 6)
print(result)
