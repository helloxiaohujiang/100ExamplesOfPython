# Reverse a String (Without Slicing)
def reverse_string():
    """Reverse a string without slicing"""
    msg = "Reverse a string"
    print(msg)
    print('-' * len(msg))
    
    n = input("\nEnter a word to reverse: ") 
    
    reverse_word = []
    i = len(n) - 1
    
    while i >= 0:
        reverse_word.append(n[i])
        i -= 1    
    
    return ''.join(reverse_word)

if __name__ == "__main__":
    reversed_str = reverse_string()
    print("\nReverse word: ", reversed_str)