# assign a number to a variable and get its type.
number = 24
number_type = type(number)

print(f'{number} is of type {number_type}')

number_float = 24.4
number_float_type = type(number_float)

print(f'{number_float} is of type {number_float_type}')


# Arithmetic Operators:
# Addition:       3 + 2
addition = number + number_float
# Subtraction:    3 - 2
subtraction = number - number_float
# Multiplication: 3 * 2
multiplication = number * number_float
# Division:       3 / 2
Division = number * number_float

# Floor Division: 3 // 2
Floor_Division = number // number_float

# Exponent:       3 ** 2
Exponent = number ** number_float

# Modulus:        3 % 2
Modulus = number % number_float

print(addition)
print(subtraction)
print(Division)
print(Floor_Division)
print(Exponent)
print(Modulus)

# auto increment
for i in range(1,10):
    i *= i
    print(i)

# absolute value
print(abs(-2))

import math as m
# rounf floor ciel
print   ('round',round(2.75,0))
print   ('floor',m.floor(2.75))
print   ('ceil',m.ceil(2.75))





# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

number_1 = 3
number_2 = 2

print('compare if numbers are equal',number_1 == number_2)
print('compare if numbers are not equal',number_1 != number_2)
print('compare if number_1 is greater than number_2',number_1 > number_2)
print('compare if number_1 is less than number_2',number_1 < number_2)
print('compare if number_1 is greater or equal to number_2',number_1 >= number_2)
print('compare if number_1 is less or equal to number_2',number_1 <= number_2)

# casting a string to a number
number_3 = '100'
number_4 = '200'
number_5 = number_3 + number_4
print(f'additon of {number_3} and {number_4} is {number_5}')

number_3 = int(number_3)
number_4 = int(number_4)
number_5 = number_3 + number_4
print(f'additon of {number_3} and {number_4} is {number_5}')



