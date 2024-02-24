def print_params(a = 1, b ='строка', c = True):
    print(a, b, c)


print_params()
print_params(99, 'fweq',False )
print_params(42, 'internet')
print_params(32)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1,2,3]
values_dict = {'a':'43', 'b':'wawawa','c':'False'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['str',True]
print_params(*values_list_2, 42)


