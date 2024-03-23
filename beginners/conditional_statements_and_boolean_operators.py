
# if statement

a = 5
b = 3
c = 3.14
d = 5
e = a

if a == b:
    print('both the objects have the same value')
elif a < b:
    print(f'{a} is not greater than {b}')
elif a > b:
    print(f'{a} is greater than {b}')
else:
    print(f'objects {a} {b} have different value')

if type(a) == type(b):
    print(f'both the objects {a} {b} are of the same data type')
else:
    print('both the objects are of different data type')


# boolean operators
    
if a == b and type(a) == type(b):
    print('both the objects are of the same datatype and value')
elif a == b or type(a) == type(b):
    print('both the ojects are either of the same data type or have the same value')

if not (type(a) == type(c)):
    print(f' {a} and {c} are of different data types')

print( a is d is e)


# operator "a == b" will compare the values within the objects, "a is b" will compare the memory location where the objects are stored , to get the memory location we use "id(object)"
if (a == d == e) and (id(a) == id(d) == id(e)) and (a is d is e):
    print('same value same memory location')
elif a == d == e:
    print (' all variables have the same value')
else:
    print(' different values & memory locations')


print(a, id(a), d, id(d), e, id(e))


# False Values:
    # False
    # None
    # Zero of any numeric type "0"
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# condition = False
# condition = 0
# condition = ''
condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')





