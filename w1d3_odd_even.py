# check if a number is odd or even
try:
    num = int(input("Enter an integer number to decide odd or even: "))
    if num % 2 == 0:
        print(f"{num} is an even number!")
    else:
        print(f"{num} is an odd number!")
except ValueError:
    print("Invalid input! Please enter a valid number!")