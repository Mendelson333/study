numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
def double(n):
    return n*n
def isod(n):
    return n % 2

result = map(double, filter(isod, numbers))
print(list(result))