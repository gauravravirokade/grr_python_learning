# define a function

def print_function():
    print('Hello World')

print(print_function) # this wont call the function but will give the location where the function is stored

# to call the function we have to use parenthesis "()"
print_function()

# passing an argument in a function and returning output 
def convert_to_lower(x: str):
    y = x.lower()
    return y

string = 'WRJDNhikslfhankls'

lowered_string = convert_to_lower(string)
print(lowered_string)

# when we are unaware of the number of arguments to be passed in a function we use '*' and '**', '*' indicates position arguments(direct values), '**' inidcates keyword arguments (key=value)
def unknown_function(*args,**kwargs):
    # for arg in args:
    #     print(arg)
    # print(args)
    # print(kwargs)
    args_set = set(args)
    args_list = list(args)
    kwargs_dict = dict(kwargs)
    return args_set, args_list, kwargs_dict

returned_set, returned_list, returned_dictionary = unknown_function(1,2,3,3,3,3,4,5,6,kw = 'value', kw2 = 'value2')

print(f'List : {returned_list}')
print(f'Set : {returned_set}')
print(f'Dictionary : {returned_dictionary}')
