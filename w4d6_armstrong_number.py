# Check Armstrong Number

def armstrong_number():
    """Calculate Armstrong Number"""
    inp = input("Enter a positive number to calcaulate: ")

    if not inp.isdigit():
        print("Invalid Input! Please enter a positive integer.")
        return
 
    result = sum(int(num)**len(inp) for num in inp)
        
    if result == int(inp):
        print(f"{inp} is an armstrong number!")
    else:
        print(f"{inp} is NOT an armstrong number!")

if __name__ == "__main__":
    armstrong_number()