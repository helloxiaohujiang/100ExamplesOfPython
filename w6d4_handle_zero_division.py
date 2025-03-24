# Handle Division by Zero Exception
while True:
    
    try:
        numerator = float(input("Enter numberator: "))
        denominator = float(input("Enter denominator: "))
        
        result = numerator/denominator
        print(f"Result: {result}")
        break
        
    except ZeroDivisionError:
        print("Error: Denominator cannot be zero. Please enter a nonzero value.")
        
    except ValueError:
        print("Error: Please enter a valid number.")