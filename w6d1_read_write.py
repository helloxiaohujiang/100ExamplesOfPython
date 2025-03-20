# Read & Write to a File
      
# write
with open("my-file.txt", "w", encoding='utf-8') as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")
    
# read
with open("my-file.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')