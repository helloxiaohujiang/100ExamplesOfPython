# Power Function (x^y) Using Recursion

def power_recursion(x,y):
    """Power function using recursion"""
    if y == 0:
        return 1
    return x * power_recursion(x, y-1)
    
# Testing the function
for i in range(4):
    print(f"2^{i} = {power_recursion(2, i)}")