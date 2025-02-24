# Check for a leap year
print("Enter a year to check if a leap year")

try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input! Please enter a valide number.")
    exit()
    
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year!")
else:
    print(year, "is not a leap year!")