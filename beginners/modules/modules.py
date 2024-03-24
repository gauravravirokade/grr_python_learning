from my_module import addition, multiplication


input_list = [1, 2.5, 3, 4.7, 5]
sum_ = 0

for num in input_list:
    print(num)
    # if isinstance(num, int) or isinstance(num, float):  # Checking if the number is either int or float
    sum_ += num  # Adding the number directly, no need for conversion
    # else:
    #     print(f"Warning: {num} is neither int nor float.")
    print(f'sum is {sum_}')

print(sum_)


# output_sum = addition(input_list)

# print(output_sum)