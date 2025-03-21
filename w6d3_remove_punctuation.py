# Remove Punctuation from a File

import string

with open("my-file.txt", "r", encoding='utf-8') as f:
    text = f.read()
    
clean_text = text.translate(str.maketrans("","",string.punctuation))

with open("my-clean-file.txt", "w", encoding='utf-8') as f:
    f.write(clean_text)