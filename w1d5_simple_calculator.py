# Simple calculator (add, subtract, multiply, division)
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operator_option = input("Select add(a), subtract(s), multiply(m), or division(d): ").lower()
if operator_option == "a":
    result = first_number + second_number
    print(f"Result: {result}")
elif operator_option == "s":
    result = first_number - second_number
    print(f"Result: {result}")
elif operator_option == "m":
    result = first_number * second_number
    print(f"Result: {result}")
elif operator_option == "d":
    if second_number == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = first_number / second_number
        print(f"Result: {result}")
else:
    print("Invalid operator! Please choose a, s, m, or d.")