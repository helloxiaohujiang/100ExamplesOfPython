# Count Lines, Words, and Characters in a File

count_line = 0
count_word = 0
count_character = 0

with open("my-file.txt", "r", encoding='utf-8') as f:
    for line in f:
        count_line += 1
        
        words = line.split()
        count_word += len(words)
            
        count_character += len(line)
        
print(f"The file has {count_line} lines.")
print(f"The file has {count_word} words.")
print(f"The file has {count_character} characters.")