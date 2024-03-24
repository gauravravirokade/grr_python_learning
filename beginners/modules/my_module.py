
print('Into my_module')

def addition(*args) -> int:
    summation = 0
    for arg in args:
        summation += arg
    return summation

def multiplication(*args) -> int:
    product = 0
    for arg in args:
        product *= arg
    return product



# num = addition(1,2,3,4,5)

# print(num)
