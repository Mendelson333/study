import warnings

def delenie(a,b):
    result = a / b
    if (b <= 0.01):
        warnings.warn("Вы близки к делению на 0", UserWarning)
    return result


warnings.simplefilter(action="always")
print(delenie(15, 0.0001))
print(delenie(15,3))
warnings.simplefilter(action="ignore")
print(delenie(15, 0.0001))
print(delenie(15,3))
warnings.simplefilter(action="error")
print(delenie(15, 0.0001))
print(delenie(15,3))