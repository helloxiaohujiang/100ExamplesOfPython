# Check if a number is prime
# base version
# import math

# welcome_msg = "Primer number check."
# print(welcome_msg)
# print("-" * len(welcome_msg))

# while True:
#     inp = input("Enter a number or Q to quit: ").strip().lower()
#     if inp == 'q':
#         print("Bye!")
#         break
#     else:   
#         try:
#             num_inp = int(inp)
#         except ValueError:
#             print("Invalid input, enter a positive integer number or Q to quit.")
#             continue
        
#     if num_inp < 2:
#         print(f"{num_inp} is NOT a prime number.")
#     elif num_inp == 2:
#         print(f"{num_inp} is a prime number.")
#     elif num_inp % 2 == 0:
#         print(f"{num_inp} is NOT a prime number.")
#     else:
#         is_prime = True
#         for i in range(3, int(math.sqrt(num_inp))+1, 2):
#             if num_inp % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(f"{num_inp} is a prime number.")
#         else:
#             print(f"{num_inp} is NOT a prime number.")
            
# function version
# import math

# def is_prime(num_inp):
#     if num_inp < 2:
#         print(f"{num_inp} is NOT a prime number.")
#     elif num_inp == 2:
#         print(f"{num_inp} is a prime number.")
#     elif num_inp % 2 == 0:
#         print(f"{num_inp} is NOT a prime number.")
#     else:
#         is_prime = True
#         for i in range(3, int(math.sqrt(num_inp))+1, 2):
#             if num_inp % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(f"{num_inp} is a prime number.")
#         else:
#             print(f"{num_inp} is NOT a prime number.")
   
            
# welcome_msg = "Primer number check."
# print(welcome_msg)
# print("-" * len(welcome_msg))

# while True:
#     inp = input("Enter a number or Q to quit: ").strip().lower()
#     if inp == 'q':
#         print("Bye!")
#         break
#     else:   
#         try:
#             num_inp = int(inp)
#         except ValueError:
#             print("Invalid input, enter a positive integer number or Q to quit.")
#             continue
#     is_prime(num_inp)
    
    
# improved function version
import math

def is_prime(num_inp):
    """Returns True if num_inp is a prime number, otherwise False."""
    if num_inp < 2:
        return False
    elif num_inp == 2:
        return True
    elif num_inp % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num_inp))+1, 2):
            if num_inp % i == 0:
                return False
        else:
            return True

# user interaction loop
def main():
    """Prime number check """
    welcome_msg = "Prime number check."
    print(welcome_msg)
    print("-" * len(welcome_msg))

    while True:
        inp = input("Enter a number or Q to quit: ").strip().lower()
        if inp == 'q':
            print("Bye!")
            break
        else:   
            try:
                num_inp = int(inp)
            except ValueError:
                print("Invalid input, enter a positive integer number or Q to quit.")
                continue
        
        if is_prime(num_inp):
            print(f"{num_inp} is a prime number.")
        else:
            print(f"{num_inp} is NOT a prime number.")
            
# run the main function
# if __name__ == "__main__":
#     main()    