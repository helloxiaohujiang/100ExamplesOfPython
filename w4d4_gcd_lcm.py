# Find GCD & LCM of Two Numbers
# GCD (Greatest Common Divisor)
# LCM (Least Common Multiple)

welcome_msg = "GCD and LCM finder"
print(welcome_msg)
print('-'*len(welcome_msg))

while True:
    while True:
        inp1 = input('Enter first number or q to quit: ').strip().lower()
        if inp1 == 'q':
            print("Bye!")
            exit()
        
        try:
            num_inp1 = int(inp1)
            if num_inp1 <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid entry! Enter a positive integer number.")
    
    while True:
        inp2 = input('Enter second number or q to quit: ').strip().lower()
        if inp2 == 'q':
            print("Bye!")
            exit()
            
        try:
            num_inp2 = int(inp2)
            if num_inp2 <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid entry! Enter a positive integer number.")
             
    # Find GCD using iteration
    a, b = num_inp1, num_inp2
    
    while b!= 0:
        a, b = b, a % b  # Euclidean algorithm for GCD
        
    gcd = a
 
    print(f"{inp1} and {inp2} GCD is: {gcd}")

    # Find LCM
    lcm = num_inp1*num_inp2//gcd
    
    print(f"{inp1} and {inp2} LCM is: {lcm}")
    
    print('-'*len(welcome_msg))
    
    
# Approach #2 for GCD
# gcd = math.gcd(num_inp1, num+inp2)
# lcm = (num_inp1 * num_inp2) // gcd