# Count digits in a number
welcome_msg = "Welcome to digits count"
print(welcome_msg)
print("-"*len(welcome_msg))


while True:
    num_inp = input("Enter a number or Q for quit: ")

    if num_inp.strip().lower() == 'q':
        print("Goodbye!")
        break
    elif num_inp.replace('.', '', 1).lstrip('-').isdigit():
        num_digit = len(num_inp.replace('.', '',1).lstrip('-'))
        print(f"{num_inp} has {num_digit} digits.\n")
    else:
        print("Invalid input! Please enter a valid number.\n")