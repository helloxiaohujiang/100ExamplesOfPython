# Merge Two Dictionaries
import time

def dict_merge(dict1, dict2):
    """Merge two dictionary"""
    dict_final = dict1.copy()
    
    for key, value in dict2.items():
            if key not in dict_final:
                dict_final[key] = value 
                    
    return dict_final


def create_dict():
    """Create dictionary"""
    print("Create a new dictionary -->")
    my_dict = {}
    
    while True:
        key = input("Enter key or 's' to end: ")
        if key.lower() == 's':
            break
        else:
            value = input("Enter value: ")
            
        my_dict[key] = value
        
    return my_dict


def main():
    """main function"""
    dict1 = create_dict()
    time.sleep(1)
    dict2 = create_dict()
    
    return dict1, dict2


if __name__ == "__main__":
    merge_result = main()
    print(merge_result)