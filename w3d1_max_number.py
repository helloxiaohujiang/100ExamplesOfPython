# Find Maximum & Minimum in a List
msg = "Find maximum and minimum number"
print(msg)
print('-'*len(msg))
lst = []
while True:
    try:
        inp_num = input("Enter number to generate list or Q to quit: ").strip().lower()
        if inp_num == "q":
            break
        inp_num = int(inp_num)
        lst.append(inp_num)
    except ValueError:
        print("Invalid input!Please enter a number") 

if lst: 
    max_num = min_num = lst[0]
    for num in lst[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print(f"\nMaximum number is: {max_num}.")
    print(f"Minimum number is: {min_num}.")
else:
    print("\nNo numbers entered. Exiting...")