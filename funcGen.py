#Фабрикафункцийдлясложенияивычитания:

def create_operation(operation):
    if operation == "divide":
            def divide(x, y):

                return x / y

            return divide

    elif operation == "add":
        def add(x, y):

                return x * y

        return add

my_func_add = create_operation("add")
my_func_divide = create_operation("divide")

print("Задача 1: Фабрика функций")
print(my_func_divide(1, 2))
print(my_func_add(1, 2))
print(my_func_divide(0, 1))


#не оч понял как в генераторе ловить исключения

#Примерлямбдафункциисаналогомчерез
print("Задача 2 лямбда")

expon = lambda x, y: x ** y

print(expon(2, 4))  # Выводит 16


def expon_def(x, y):
    return x ** y


print(expon_def(2, 4))  # Выводит 16

#Примерсозданиявызываемогообъекта

print("Задача 3 : Вызываемые объекты ")
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, ):
        return self.a * self.b


sides = Rect(3,5)
print("Стороны: "+str(sides.a)+" "+str(sides.b))
print("Площадь: "+str(sides())+"")