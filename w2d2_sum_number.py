# sum up first n natural numbers
print("Tell me some numbers and I can help to sum up first N natural numbers.")

num_lst = []

# Collect numbers from the user
while True:
    inp = input("Enter a number or 'C' to complete: ").strip().lower()
    if inp == 'c':
        break
    try:
        num_lst.append(float(inp))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        
# Ensure the list is not empty
if not num_lst:
    print("No numbers entered. Exiting...")
    exit()
    
# Sum the first N numbers    
while True:
    try:
        num_to_sum = int(input("How many of the first numbers to sum? "))
        
        if num_to_sum <= 0:
            print("Enter a positive integer.")
            continue
        
        if num_to_sum > len(num_lst):
            print(f"You can only enter upto {len(num_lst)} numbers maximum. Try again.")
            continue
        num_sum = sum(num_lst[:num_to_sum])
        print(f"The sum of the first {num_to_sum} numbers is: {num_sum}")
        break
    
    except ValueError:
        print("Invalid input!! Enter an integer.")