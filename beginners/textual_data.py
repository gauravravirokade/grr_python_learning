# print a message
print('Hello World')

# to store a message in a variable and print the variable
message = 'Hello World message'
print(message)

# '' and "" are more the same except when we want to print (') within a string.
print('Hey that\'s mine','single_quoted')
# in the above statement interpreter assumes the string ends at (Hey that) as we have an (') in the word (that's) if we want to still use single quote we can use a backslash(\) before the use of (')
# or use ( " ") and add (') within them
print("Hey that's mine","double_quoted" )

# print a big message stored in multiple lines
multi_line_message = """ Hey that's mine
    and this is your's"""
print(multi_line_message) 

#string length
message_length = len (multi_line_message)
print ("below message is of length ",message_length,'\n',multi_line_message)

#slincing strings
print('print the first word by specifying start and end index - ',message[0:5],'\n',' just specifying the end index (python will assume the start as Zero"0" - ',message[:5])

#upper/lower
print(message[0:5].upper(),message[5:].lower())

# count number of occurances in a string
print( 'the alphabet "i" has occured',multi_line_message.count('i'),'times in the below message \n',multi_line_message)

# check if 'X' is a part of a message
print(multi_line_message.find('i')) # even though we have multiple occurances of 'X' it will return the index of the first occurance, will return -1 if 'X' is not found in the string

# replace, if we want to modify the changes in the object we will have to assign the changes to it again
message.replace('Hello','Ola') # will not replace it permanenty from the message string, if will work in the below print statement
print(message.replace('Hello','Ola'))
# but if we want to replace and modify the string we use below 

modified_message = message.replace('Hello','Ola')

print(modified_message)

# concat two strngs
name = 'gaurav'
greeting = 'Hi'

concat_message =f'{greeting}, {name.capitalize()}. Welcome!'

print(concat_message)