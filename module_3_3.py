def print_params(a = 1, b = 'Hello', c = True):
    print(a,b,c)
print_params()
print_params('Hello', 1, True)
print_params(b=25)
print_params(c=[1,2,3])


values_list = [22,'World',False]
values_dict = {'a' : 7, 'b' : 'car', 'c' : 2024 }
print_params(*values_list)
print_params(**values_dict)


values_list2 = [54.32, 'Строка']
print_params(*values_list2,42)