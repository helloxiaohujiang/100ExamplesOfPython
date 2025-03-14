# Frequency Count of Elements in a List

def count_frequency(lst):
    """Frequency count of elements in a list."""
    count_dict = {}
    
    if lst is None:
        return {}
        
    for element in lst:
        count_dict[element] = count_dict.get(element, 0) + 1

    return count_dict

def main():
    """User interface for frequency count"""
    inp_lst = []
    
    while True:
        inp = input("Enter element to add, or 's' for stop: ").strip().lower()
        
        if inp == 's':
            break
        else:
            inp_lst.append(inp)

    result = count_frequency(inp_lst)
    print("Element frequency count:\n", result)
        
if __name__ == "__main__":
    main()