# Write a Function to Check Prime Number
# Prime number are numbers that have only 2 factors: 1 and themselves.
import math

# Define prime function
def is_prime(num_inp):
    """Returns true if number is a prime, otherwise false."""
    if num_inp < 2:
        return False
    if num_inp == 2:
        return True
    if num_inp % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num_inp)+1), 2):
        if num_inp % i == 0:
            return False
    return True
        
# Define interactive loop
def main():
    welcome_message = "Prime number checker"
    print(welcome_message)
    print("-" * len(welcome_message))
    
    while True:
        inp = input("Enter a number or Q to exit: ").strip().lower()
        if inp == 'q':
            print("Bye")
            break
        else:
            try:
                num_inp = int(inp)
                if num_inp < 2:
                    print("Enter number greater than 1.")
                    continue
            except ValueError:
                print("Invalid input!")
                continue
        
        if is_prime(num_inp):
            print(num_inp, "is a prime number.")
        else:
            print(num_inp, "is NOT a prime number.")
            
if __name__ == "__main__":
    main()