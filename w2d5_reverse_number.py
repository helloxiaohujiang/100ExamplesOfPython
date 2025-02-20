# Reverse a number
welcome_msg = "welcome to number reverse application"
print(welcome_msg)
print('*'*len(welcome_msg))

while True:
    num_inp = input("Enter a number or Q for quit: ").strip()
    
    if num_inp.lower() == 'q':
        print("Bye!\n")
        break
    elif num_inp.lstrip('-').isdigit():
        reversed_num = num_inp[::-1] if num_inp[0]!='-' else '-' + num_inp[:0:-1]
        print(f"Reversed Number: {reversed_num}\n")
    else:
        print("Invalid input, enter a integer greater than zero.\n")