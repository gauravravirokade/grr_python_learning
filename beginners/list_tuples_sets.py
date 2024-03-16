
# list

# create a list

subjects = ['Math', 'Science', 'History', 'Computer']

# print the entire list & it's length
subjects_len = len(subjects)

print(f'list : {subjects} is of length {subjects_len}')

# print each element from the list with it's location

for i in range(subjects_len):
    print(f'the {i} element in the list is {subjects[i]}')

# iterate teh list in reverse order
for j in range(-subjects_len,0):
    print(f'the {j} element in the list is {subjects[j]}')

# print a part of a list
print(subjects[0:3]) # lower limit is inclusive and upper limit is exclusive
subjects = ['Math', 'Science', 'History', 'Computer']

# list_name.reverse() overwrites the original list with its reverse form
subjects.reverse()
print(subjects)

# if we want to reverse a list, and store the reversed in a different object
reverse_subjects = subjects[::-1]
print(reverse_subjects)

# add to existing list, append to add at the end, insert for a specific location
subjects.append('Biology')
print(subjects)

subjects.insert(1,'Statistics')
print(subjects)

# add the objects from one list to another
additional_subjects = ['Programming Languages', 'Economics']

# using insert or append will add the entire list as an element in the existing list
subjects.insert(3,additional_subjects)
print(subjects)

# if we want to add only the objects we use extend.
reverse_subjects.extend(additional_subjects)
print(reverse_subjects)

# remove an object from a list

reverse_subjects.remove('Economics')
print(reverse_subjects)

# pop by default it will remove the last value from

reverse_subjects.pop()
print(reverse_subjects)

popped_object = reverse_subjects.pop(0)

print(f'object {popped_object} was popped from the list {reverse_subjects} which was stored at index 0')

# sort a list, default it sorts in ascending order, to sort in descending order we pass an argument reverse=True
reverse_subjects.sort()
print(reverse_subjects)
num_list = [1,2,3,4,5]
num_list.sort(reverse=True)
print(num_list)

# if you intend to keep your original list and store the sorted list in a different list

desc_sorted_list = sorted(num_list)
print(desc_sorted_list)



# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()








