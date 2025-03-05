# Find the Second Largest Number in a List

sample_list = [2,3,5,1,7,8,3]

# define largest and second largest number
largest_number = float('-inf') # Initialize to negative infinity
second_largest_number = float('-inf')

for num in sample_list:
    if num > largest_number:
        second_largest_number = largest_number
        largest_number = num
    elif num > second_largest_number and num != largest_number:
        second_largest_number = num
        
if second_largest_number == float('-inf'):
    print("No second largest number found.")
else:
    print("The largest number: ", largest_number)
    print("The second largest number: ", second_largest_number)