# Fibonacci Series (Using Loop)
# Fibonacci sequence is a sequence in which each element is the sum of the two
# elements that precede it

# Normal approach
# num_list = []

# while True:
#     num = input("Enter numbers to calculate or Q to quit: ").strip().lower()
#     if num == 'q':
#         print("Bye!")
#         break
#     try:
#         num_list.append(int(num))
#     except ValueError:
#         print("Invalid input!!")

# if num_list:
#     fib_list=[]
#     if len(num_list) < 2:
#         print(f"Fib series is {num_list}")
#     else:
#         fib_list = num_list[:2]
#         for i in range(2,len(num_list)):   
#             fib_list.append(num_list[i-2] + num_list[i-1])
#         print(f"Fib series is {fib_list}")
        

# Function approach
"""Generate a fibonacci series"""
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    fib_series = [0,1]
    for _ in range(n-2):
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series

while True:
    num = input("Enter a number to generate Fibonacci series or Q to quit: ").strip().lower()
    if num == 'q':
        print("Bye!")
        break
    try:
        num = int(num)
        print(f"Fibonacci Series for {num}: {fibonacci(num)}")
    except ValueError:
        print("Invalid input!! Please enter a valid number.")