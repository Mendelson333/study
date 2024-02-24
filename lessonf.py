

def test(a = 0, b = 10, *args, **kwargs):
    print(a,b)
    print(*args)
    print(*kwargs, )


test(1, 3, 9, 10, cat = 'black')

def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n = n-1)
    return n * factorial_n_minus_1

print(factorial(10))