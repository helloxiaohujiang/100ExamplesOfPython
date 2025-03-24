# Try-Except to Handle User Input Errors
import math

while True:
    try:
        inp = input("Enter an input to calculate or 'q' to quit -->> ").strip().lower()
        if inp == 'q':
            print('Bye~')
            break
        
        inp_num = float(inp)
        
        if inp_num < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        
        result = math.sqrt(inp_num)
        print(f"The result is: {result}")
        
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid non-negative number.")