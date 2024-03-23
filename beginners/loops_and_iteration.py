

# For loop

num_List = [1, 2, 3, 4, 5, 6]

for num in num_List:
    print(f'at locaton {num_List.index(num)} value {num} is stored')

# to stop the loop once a condition is met, we use break
    
for num in num_List:
    if num == 4:
        print('Maximum limit reached \n')
        break
    print(num)

# to skip the loop once a condition is met, we use continue
    
for num in num_List:
    if num == 4:
        print('Maximum limit reached \n')
        continue
    print(num)

# nexted loops 
for i in num_List:
    for j in 'asd':
        print(i,j,'\n')

# to run a for loop within a specific range, it includes the lower limit but not the upper limit

for i in range (1,5):
    print(i)

# While Loop - it interates through the loop until a condiion is met
    
num = 3
while num <10:
    print(num)
    num += 1

        
    



