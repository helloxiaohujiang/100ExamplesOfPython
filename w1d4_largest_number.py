# Find the largest number
try:
    print("Enter three number to find the largest one.")
    numbers = []
    for i in range(3):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
  
    if numbers[1] > numbers[0]:
        temp = numbers[1]
        if numbers[2] > temp:
            largest_num = numbers[2]
        else:
            largest_num = temp
    else:
        temp = numbers[0]
        if numbers[2] > temp:
            largest_num = numbers[2]
        else:
            largest_num = temp
        
    print(f"The largest number is: {largest_num}")
    
except ValueError:
    print("Invalid input! Please enter a valid number.")