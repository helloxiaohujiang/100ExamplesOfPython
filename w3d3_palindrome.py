# Check if a String is Palindrome
# Palindrome: a word, phrase or sequence that reads the same backward
# as forward.
# word = "madam"
import re

def palindrome():
    """Check if a word or string Palindrome"""
    msg = "Check if a string a Palindrome"
    print(msg)
    print('-' * len(msg))

    while True:
        inp = input("Enter word/sentence to check or Q to quit: ").strip().lower()
        # print("You entered: ", inp)
        
        if inp == 'q':
            break
        
        inp_char = re.sub(r'[^a-z]', '', inp)
        inp_char_len = len(inp_char)
        flag = True

        for i in range(inp_char_len//2):
            if inp_char[i] != inp_char[inp_char_len-1-i]:
                flag = False

        if flag == True:
            print(f"'{inp}' is a Palindrome!")
        else:
            print(f"'{inp}' is not a Palindrome!")
            
if __name__ == "__main__":
    palindrome()