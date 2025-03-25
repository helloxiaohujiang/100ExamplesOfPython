# Append Data to a File

with open("my-file.txt", 'a') as f:
    msg = 'This is adding part.\n'
    f.write(msg)
    
with open("my-file.txt", 'r') as f:
    result = f.readlines()
    print(result)