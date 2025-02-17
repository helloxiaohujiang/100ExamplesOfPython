# Convert temperature between celsius and fahrenheit
print("-------------")
print("Welcome to temperature conversion.")
status_temp = input("press enter to start or Q to quit.").strip().lower()

if status_temp == "q":
    exit()
else:    
    while True:
        try:
            temp_unit = input("Enter your temperature unit (Celsius(C) or Fahrenheit(F)? or Quit(Q))").strip().lower()
            if temp_unit == "q":
                print("Goodbye!")
                break
            
            temp_value = float(input("Enter your temperature value to be converted: "))
        except ValueError:
            print("Invalid input! Enter a valid temperature value!!")
            continue

        if temp_unit == "c":
            fah_temp = temp_value*9/5 + 32
            print(f"Your fahrenheit temperature is: {fah_temp:.2f}°F.")   
        elif temp_unit == "f":
            cel_temp = (temp_value-32)*5/9
            print(f"Your celsius temperature is: {cel_temp:.2f}°C.")
        else:
            print("Invalid input, enter either C , F or Q!")
            
        print("-------------")