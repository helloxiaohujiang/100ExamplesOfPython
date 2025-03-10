# Factorial Using Recursion
# def factorial(n):
#     """Factorial"""
#     factorial_sum = 1
    
#     while n > 0:
#         factorial_sum *= n
#         n = n-1
#     return factorial_sum

def factorial(n):
    """ Factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

def main():
    welcome_message = ("Factorial calculation")
    print(welcome_message)
    print("*" * len(welcome_message)*2)
    
    while True:
        inp = input("Enter a number or 'q' to quit: ").strip().lower()
        if inp == "q":
            print("Bye!")
            break
        try:
            num_inp = int(inp)
            if num_inp < 0:
                print("Enter a number greater than or equal to 0.")
                continue
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        result = factorial(num_inp)
        print(result)

if __name__ == "__main__":
    main()