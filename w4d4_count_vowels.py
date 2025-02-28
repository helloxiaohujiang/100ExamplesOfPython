# Count Vowels & Consonants in a String
def count_vowels_consonants():
    """Count vowels and consonants."""
    vowels = ['a', 'e', 'i','o', 'u']
    
    string_inp = input("Enter a string: ").strip().lower()

    vowels_count = 0
    consonant_count = 0

    for char in string_inp:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonant_count +=1
    
    return vowels_count, consonant_count
 
if __name__ == "__main__":
    vowels, consonates = count_vowels_consonants() 
    print(f"Vowels: {vowels}, Consonants: {consonates}.")