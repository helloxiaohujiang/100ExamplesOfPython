# multiplication table by any numbers
print("Multiplication Table Generator")
print("--------------------------------")
while True:
    try:
        num1 = int(input("Enter the number of rows: "))
        num2 = int(input("Enter the number of columns: "))
    
        if num1 <= 0 or num2 <= 0:
            print("Please enter positive numbers greater than zero.")
            continue
    
    except ValueError:
        print("Invalid input. Please enter integers only.")
        continue
    
    print("\nMultiplication Table:")
    
    for i in range(1,num1+1):
        for j in range(1,num2+1):
            print(f"{i*j:4}", end=' ')
        print()
    
    choice = input("\nDo you want to generate another table? (y/n): ").strip().lower()
    if choice != 'y':
        print("Goodbye!")    
        break