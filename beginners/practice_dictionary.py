# print("jelo")
sample_dictionary = {
    'name' : 'Gaurav',
    'age' : 29,
    'company' : 'Talkiatry',
    'salary' : 50.34
}
# to reterive a value from a dictionary
# 1
employee_name =  sample_dictionary['name']
print("1. " + employee_name)
emp_name = sample_dictionary.get('name')
print("2. " + emp_name)

# employee_city = sample_dictionary['city']
# print (employee_city)


# .get() is useful when we dont have a the requested key in our dictionary, the default value is 'None' but we can default it to anything we want
# in the below example I am defaulting the city to 'Tampa'.

employee_city = sample_dictionary.get('city','Tampa')
# print(employee_city)

# add a new field to an existing dictionary
sample_dictionary['city'] = 'Tampa'

print(sample_dictionary)

# to update a dictionary

# update single value at a time
sample_dictionary['company'] = 'New_Employer'

print(sample_dictionary['company'])

# to update multiple values in a dictionary

sample_dictionary.update({'age' : 28, 'salary' : 70.35, 'exp' : 5})

print(sample_dictionary)


# delete keys from a dictionary, del with permanently delete and you wont be able to store it in an object

del sample_dictionary['exp']

print(sample_dictionary)

# to store the deleted element in an object

popped_city = sample_dictionary.pop('city')

print(sample_dictionary)
print(f'popped value : {popped_city}')

# to get only keys, values & a combination of both

print('print all keys in the dictionary',sample_dictionary.keys())
print('print all values in the dictionary',sample_dictionary.values())
print('print key & value in the dictionary',sample_dictionary.items())

# loop through a dictionary

for key,value in sample_dictionary.items():
    print(key,value)